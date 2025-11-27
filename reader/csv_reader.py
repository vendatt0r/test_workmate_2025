import csv
from pathlib import Path


def read_csv_files(paths):
    rows = []
    for path in paths:
        file = Path(path)
        if not file.exists():
            raise FileNotFoundError(f"File not found: {path}")

        with file.open(encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)

    return rows
