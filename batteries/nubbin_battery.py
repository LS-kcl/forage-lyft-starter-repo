from battery import Battery
from datetime import timedelta


class NubbinBattery(Battery):
    def __init__(last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return self.current_date - self.last_service_date > timedelta(years = 4)

    def needs_service(self):
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
