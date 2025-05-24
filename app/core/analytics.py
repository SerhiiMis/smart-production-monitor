from collcections import defaultdict

def group_by_machine(records):
    grouped = defaultdict(list)
    for record in records:
        grouped[record.machine_id].append(record)
    return grouped

def compute_machine_kpis(grouped_data):
    kpis = {}
    for machine_id, records in grouped_data.items():
        total_units = sum(r.units_produced for r in records)
        total_scrap = sum(r.scrap_count for r in records)
        running_rows = sum(1 for r in records if r.is_running())
        
        kpis[machine_id] = {
            "total_units": total_units,
            "total_scrap": total_scrap,
            "running_rows": running_rows
        }
    return kpis