from tabulate import tabulate
from cli import parse_args
from reader.csv_reader import read_csv_files
from reports.registry import get_report


def main():
    args = parse_args()

    rows = read_csv_files(args.files)

    report = get_report(args.report)
    data = report.generate(rows)
    headers = report.headers()

    print(tabulate(data, headers=headers, tablefmt="github"))


if __name__ == "__main__":
    main()
