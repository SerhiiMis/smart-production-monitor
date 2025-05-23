from datetime import datetime

class ProductionRecord:
    def __init__(self, timestamp, machine_id, status, units_produced, scrap_count):
        self.timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        self.machine_id = machine_id
        self.status = status
        self.units_produced = int(units_produced)
        self.scrap_count = int(scrap_count)

    def is_running(self):
        return self.status == "Running"