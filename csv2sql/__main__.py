import argparse
import csv
import io
import logging
import platform
import sqlite3
import types

from pathlib import Path

from . import evtss_2023


def main():
    logger: logging.Logger = _create_logger()

    parser: argparse.ArgumentParser = _create_parser()
    args: argparse.Namespace = parser.parse_args()
    csv_file: io.TextIOWrapper = args.csv_file[0]
    db_file: Path = args.db_file[0]
    log_file: Path = args.log_file

    log_file.parent.mkdir(parents=True, exist_ok=True)
    log_file.touch(exist_ok=True)
    _add_log_file_to_logger(logger, log_file)

    csv_data: csv.DictReader = csv.DictReader(csv_file)
    db_conn: sqlite3.Connection = sqlite3.connect(db_file)

    db_cursor: sqlite3.Cursor = db_conn.cursor()

    converter: types.ModuleType = evtss_2023
    converter.create_tables(db_cursor)
    converter.convert(csv_data, db_cursor)

    db_conn.commit()

    db_cursor.close()
    db_conn.close()


def _create_logger() -> logging.Logger:
    logger: logging.Logger = logging.getLogger('csv2sql')
    logger.setLevel(logging.INFO)

    stream_handler: logging.StreamHandler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    stream_formatter = logging.Formatter('%(message)s')
    stream_handler.setFormatter(stream_formatter)

    logger.addHandler(stream_handler)

    return logger


def _get_default_log_file_path() -> Path:
    if platform.system() == 'Linux':
        return Path.home() / '.local/state/dev8/csv2sql/csv2sql.log'
    else:
        msg: str = 'Cannot specify default log file yet in non-Linux platforms'
        raise NotImplementedError(msg)


def _add_log_file_to_logger(logger: logging.Logger, log_file: Path):
    handler: logging.FileHandler = logging.FileHandler(log_file)
    handler.setLevel(logging.INFO)

    fmt: str = '%(asctime)s %(name)-15s :: [ %(levelname)-8s ] %(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)

    logger.addHandler(handler)


def _create_parser() -> argparse.ArgumentParser:
    logger: logging.Logger = logging.getLogger('csv2sql')

    desc = 'Create an SQLite database out of a CSV file.'
    csv_file_arg_help = 'the CSV file to make an SQLite database out of'
    output_arg_help = 'the SQLite database file name or path to output to'
    logfile_arg_help = 'the log file to store logs to'

    try:
        default_log_file: Path = _get_default_log_file_path()
    except NotImplementedError as e:
        default_log_file: None = None
        logger.warning(str(e))

    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=desc)
    parser.add_argument('csv_file', metavar='CSV_FILE',
                        type=argparse.FileType('r', encoding='UTF-8'),
                        nargs=1, help=csv_file_arg_help)
    parser.add_argument('db_file', metavar='DB_FILE', type=Path,
                        nargs=1, help=output_arg_help)
    parser.add_argument('--log-file', metavar='LOG_FILE', type=Path,
                        default=default_log_file, help=logfile_arg_help)

    return parser


if __name__ == '__main__':
    main()
