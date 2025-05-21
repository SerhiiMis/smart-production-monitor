import csv
from pathlib import Path
from datetime import datetime

def load_data(filepath):
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    processed = []
    for row in data:
        processed.append({
            "timestamp": datetime.strptime(row["timestamp"], "%Y-%m-%d %H:%M:%S"),
            "machine_id": row["machine_id"],
            "status": row["status"],
            "units_produced": int(row["units_produced"]),
            "scrap_count": int(row["scrap_count"])
        })

    return processed

if __name__ == "__main__":
    path = Path(__file__).resolve().parent.parent.parent / "data" / "example_production_log.csv"
    records = load_data(path)

    total_units = sum(r["units_produced"] for r in records)
    total_scrap = sum(r["scrap_count"] for r in records)
    running_rows = sum(1 for r in records if r["status"] == "Running")

    print(f"Loaded {len(records)} rows.")
    print(f"Total units produced: {total_units}")
    print(f"Total scrap count: {total_scrap}")
    print(f"Running rows: {running_rows}")