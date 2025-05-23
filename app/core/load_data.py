import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
import csv
from pathlib import Path
from app.core.models import ProductionRecord

def load_data(filepath):
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        return [ProductionRecord(**row) for row in reader]

if __name__ == "__main__":
    path = Path(__file__).resolve().parent.parent.parent / "data" / "example_production_log.csv"
    records = load_data(path)

    total_units = sum(r.units_produced for r in records)
    total_scrap = sum(r.scrap_count for r in records)
    running_rows = sum(1 for r in records if r.is_running())

    print(f"Loaded {len(records)} rows.")
    print(f"Total units produced: {total_units}")
    print(f"Total scrap count: {total_scrap}")
    print(f"Running rows: {running_rows}")