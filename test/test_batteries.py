import unittest
from datetime import datetime

from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
    """Requires servicing every 4 years"""
    def test_battery_requires_servicing_every_4_years(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(last_service_date)
        self.assertTrue(battery.needs_service())
    
    """Does not require servicing under 4 years"""
    def test_battery_does_not_require_servicing_under_4_years(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = NubbinBattery(last_service_date)
        self.assertFalse(battery.needs_service())
    
class TestSpindlerBattery(unittest.TestCase):
    """Requires servicing every 2 years"""
    def test_battery_requires_servicing_every_2_years(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = SpindlerBattery(last_service_date)
        self.assertTrue(battery.needs_service())
    
    """Does not require servicing under 2 years"""
    def test_battery_does_not_require_servicing_under_2_years(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = SpindlerBattery(last_service_date)
        self.assertFalse(battery.needs_service())
    
    

if __name__ == '__main__':
    unittest.main()
