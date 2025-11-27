from reader.csv_reader import read_csv_files
import pytest


def test_read_csv_files(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text(
        "name,position,performance\n"
        "Alex,Dev,4.5\n",
        encoding="utf-8",
    )

    rows = read_csv_files([file])
    assert len(rows) == 1
    assert rows[0]["name"] == "Alex"


def test_missing_file():
    with pytest.raises(FileNotFoundError):
        read_csv_files(["missing.csv"])
