import argparse


def create_parser() -> argparse.ArgumentParser:
    desc = 'Create an SQLite database out of a CSV file.'
    csv_file_arg_help = 'the CSV file to make an SQLite database out of'
    output_arg_help = 'the SQLite database file name or path to output to'

    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=desc)
    parser.add_argument('csv_file', metavar='CSV_FILE', type=str,
                        nargs=1, help=csv_file_arg_help)
    parser.add_argument('db_file', metavar='DB_FILE', type=str,
                        nargs=1, help=output_arg_help)

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
