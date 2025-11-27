import argparse

def parse_args(args=None):
    parser = argparse.ArgumentParser(description="Generate reports.")

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Input CSV files"
    )

    parser.add_argument(
        "--report",
        choices=["performance"],
        required=True,
        help="Report type"
    )

    return parser.parse_args(args)
