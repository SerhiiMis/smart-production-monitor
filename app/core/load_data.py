import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
import csv
from app.core.analytics
from app.core.models import ProductionRecord

def load_data(filepath):
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        return [ProductionRecord(**row) for row in reader]

if __name__ == "__main__":
    path = Path(__file__).resolve().parent.parent.parent / "data" / "example_production_log.csv"
    records = load_data(path)

    grouped = group_by_machine(records)
    kpis = compute_machine_kpis(grouped)

    print(f"✅ Loaded {len(records)} rows.\n")
    for machine_id, metrics in kpis.items():
        print(f"📊 Machine: {machine_id}")
        print(f"   🔧 Total Units:  {metrics['total_units']}")
        print(f"   🗑️  Total Scrap:  {metrics['total_scrap']}")
        print(f"   🏃 Running Rows: {metrics['running_rows']}\n")