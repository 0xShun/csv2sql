import argparse
import csv
import io
import logging
import platform
import sqlite3
from pathlib import Path
import importlib

def main() -> None:
    # Create a logger for logging information and errors
    logger: logging.Logger = _create_logger()

    # Set up command line argument parsing
    parser: argparse.ArgumentParser = _create_parser()
    args: argparse.Namespace = parser.parse_args()
    csv_file: io.TextIOWrapper = args.csv_file[0]
    db_file: Path = args.db_file[0]
    log_file: Path = args.log_file
    module_name: str = args.module

    # Ensure the log file directory exists and create the log file
    log_file.parent.mkdir(parents=True, exist_ok=True)
    log_file.touch(exist_ok=True)
    _add_log_file_to_logger(logger, log_file)

    # Dynamically import the module specified by the user
    module = importlib.import_module(f"csv2sql.{module_name}")
    create_tables = getattr(module, 'create_tables')
    convert = getattr(module, 'convert')

    # Read CSV data into a dictionary format
    csv_data: csv.DictReader = csv.DictReader(csv_file)
    # Connect to the SQLite database
    db_conn: sqlite3.Connection = sqlite3.connect(db_file)
    db_cursor: sqlite3.Cursor = db_conn.cursor()

    try:
        # Create database tables and convert CSV data to SQL
        create_tables(db_cursor)
        convert(csv_data, db_cursor)
        logger.info("Successfully converted CSV data to SQLite database")
    except Exception as e:
        # Log any errors during conversion and rollback changes
        logger.error(f"Error during conversion: {e}")
        db_conn.rollback()
        return

    # Commit changes to the database
    db_conn.commit()
    logger.info("Successfully committed changes to database")

    # Close the database cursor and connection
    db_cursor.close()
    db_conn.close()
    logger.info("Database connection closed")


def _create_logger() -> logging.Logger:
    # Set up a logger for the application
    logger: logging.Logger = logging.getLogger('csv2sql')
    logger.setLevel(logging.INFO)

    # Create a stream handler for logging to the console
    stream_handler: logging.StreamHandler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    # Set the format for console logging
    stream_formatter = logging.Formatter('%(message)s')
    stream_handler.setFormatter(stream_formatter)

    # Add the stream handler to the logger
    logger.addHandler(stream_handler)

    return logger


def _get_default_log_file_path() -> Path:
    # Determine the default log file path based on the operating system
    if platform.system() == 'Linux':
        return Path.home() / '.local/state/dev8/csv2sql/csv2sql.log'
    elif platform.system() == 'Windows':
        return Path.home() / 'AppData/Local/dev8/csv2sql/csv2sql.log'
    elif platform.system() == 'Darwin':  # macOS
        return Path.home() / 'Library/Logs/dev8/csv2sql/csv2sql.log'
    else:
        msg: str = f'Unsupported platform: {platform.system()}'
        raise NotImplementedError(msg)


def _add_log_file_to_logger(logger: logging.Logger, log_file: Path) -> None:
    # Create a file handler for logging to a file
    handler: logging.FileHandler = logging.FileHandler(log_file)
    handler.setLevel(logging.INFO)

    # Set the format for file logging
    fmt: str = '%(asctime)s %(name)-15s :: [ %(levelname)-8s ] %(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(handler)


def _create_parser() -> argparse.ArgumentParser:
    # Get a logger for logging warnings
    logger: logging.Logger = logging.getLogger('csv2sql')

    # Define command line argument descriptions
    desc = 'Convert EVTSS survey data from CSV format to SQLite database.'
    csv_file_arg_help = 'CSV file containing EVTSS survey responses'
    output_arg_help = 'Output SQLite database file path'
    logfile_arg_help = 'Log file path (platform-specific default if not specified)'
    module_arg_help = 'Module name for conversion functions'

    # Attempt to get the default log file path
    default_log_file: Path = None
    try:
        default_log_file: Path = _get_default_log_file_path()
    except NotImplementedError as e:
        logger.warning(str(e))

    # Set up the argument parser with descriptions and default values
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=desc)
    parser.add_argument('csv_file', metavar='CSV_FILE',
                        type=argparse.FileType('r', encoding='UTF-8'),
                        nargs=1, help=csv_file_arg_help)
    parser.add_argument('db_file', metavar='DB_FILE', type=Path,
                        nargs=1, help=output_arg_help)
    parser.add_argument('--log-file', metavar='LOG_FILE', type=Path,
                        default=default_log_file, help=logfile_arg_help)
    parser.add_argument('--module', '-m', metavar='MODULE', type=str,
                    choices=['evtss_2023', 'evtss_2024'], help=module_arg_help)

    return parser

if __name__ == '__main__':
    main()
