from battery import Battery
from datetime import datetime


class SpindlerBattery(Battery):
    def __init__(last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return service_threshold_date < datetime.today().date()
