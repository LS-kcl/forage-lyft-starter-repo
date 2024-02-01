import unittest

from engines.capulet_engine import CapuletEngine
from engines.willoughby_engine import WilloughbyEngine
from engines.sternman_engine import SternmanEngine

class TestCapuletEngine(unittest.TestCase):
    """Require servicing above 30000 miles"""
    def test_engine_requires_serviving_above_30000_miles(self):
        engine = CapuletEngine(30001, 0)
        self.assertTrue(engine.needs_service())

    """Does not require servicing under 30000 miles"""
    def test_engine_does_not_require_serviving_above_30000_miles(self):
        engine = CapuletEngine(200, 0)
        self.assertFalse(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    """Require servicing above 60000 miles"""
    def test_engine_requires_serviving_above_60000_miles(self):
        engine = WilloughbyEngine(60001, 0)
        self.assertTrue(engine.needs_service())

    """Does not require servicing under 60000 miles"""
    def test_engine_does_not_require_serviving_below_60000_miles(self):
        engine = CapuletEngine(200, 0)
        self.assertFalse(engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    """Requires servicing if warning light is on"""
    def test_engine_requires_servicing_if_warning_light_on(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    """Does not require servicing if warning light is off"""
    def test_engine_does_not_require_servicing_if_warning_light_off(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
