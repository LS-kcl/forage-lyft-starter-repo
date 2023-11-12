from battery import Battery
from datetime import timedelta


class NubbinBattery(Battery):
    def __init__(last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return self.current_date - self.last_service_date > timedelta(years = 4)
