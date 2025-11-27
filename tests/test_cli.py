from cli import parse_args
import pytest


def test_cli_arguments():
    args = parse_args(["--files", "a.csv", "b.csv", "--report", "performance"])
    assert args.files == ["a.csv", "b.csv"]
    assert args.report == "performance"


def test_cli_missing_args():
    with pytest.raises(SystemExit):
        parse_args([])
