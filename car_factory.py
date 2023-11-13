from car import Car
from batteries import SpindlerBattery, NubbinBattery
from engines import CapuletEngine, WilloughbyEngine, SternmanEngine


class CarFactory():
    def create_calliope(last_service_date, current_mileage, last_service_mileage):
        battery = SpindlerBattery(last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(battery, engine)
        
    def create_glissade(last_service_date, current_mileage, last_service_mileage):
        battery = SpindlerBattery(last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(battery, engine)

    def create_palindrome(last_service_date, warning_light_on):
        battery = NubbinBattery(last_service_date)
        engine = SternmanEngine(warning_light_on)
        return Car(battery, engine)

    def create_rorschach(last_service_date, current_mileage, last_service_mileage):
        battery = NubbinBattery(last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        return Car(battery, engine)

    def create_thovex(last_service_date, current_mileage, last_service_mileage):
        battery = NubbinBattery(last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)
        return Car(battery, engine)
