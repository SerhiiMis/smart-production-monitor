import csv
from pathlib import Path

def load_data(filepath):
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data

if __name__ == "__main__":
    path = Path(__file__).resolve().parent.parent.parent / "data" / "example_production_log.csv"
    records = load_data(path)

    print(f"Loaded {len(records)} rows.")
    print(f"First row:\n{records[0]}")