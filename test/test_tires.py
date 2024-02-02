import unittest

from tires.carrigan import CarriganTire
from tires.octoprime import OctoprimeTire

class TestCarrigainTire(unittest.TestCase):
    """Requires servicing when one or more tires is above or equal to 0.9 wear"""
    def test_tires_require_servicing_if_one_tire_above_09(self):
        wear_array = [0.95, 0, 0, 0]

        tire = CarriganTire(wear_array)
        assertTrue(tire.needs_service())

    def test_tires_require_servicing_if_one_tire_equal_to_09(self):
        wear_array = [0.9, 0, 0, 0]

        tire = CarriganTire(wear_array)
        assertTrue(tire.needs_service())

    def test_tires_require_servicing_if_multiple_tires_above_09(self):
        wear_array = [0.95, 0.92, 0, 0.95]

        tire = CarriganTire(wear_array)
        assertTrue(tire.needs_service())

    def test_tires_require_servicing_if_all_tires_above_09(self):
        wear_array = [0.95, 0.95, 0.95, 0.95]

        tire = CarriganTire(wear_array)
        assertTrue(tire.needs_service())

    """Does not require servicing unless one or more tires is above or equal to 0.9 wear"""
    def test_tires_do_not_require_servicing_if_all_tires_below_09(self):
        wear_array = [0.6, 0.6, 0.6, 0.6]

        tire = CarrigainTire(wear_array)
        assertFalse(tire.needs_service())
    

    
class TestOctoprimeTire(unittest.TestCase):
    """Requires servicing when sum of wear is above or equal to 3"""
    def test_tires_require_servicing_if_sum_of_wear_equals_3(self):
        wear_array = [0.9, 0.9, 0.9, 0.6]

        tire = OctoprimeTire(wear_array)
        assertTrue(tire.needs_service())
    
    def test_tires_require_servicing_if_sum_of_wear_above_3(self):
        wear_array = [1, 1, 1, 0]

        tire = OctoprimeTire(wear_array)
        assertTrue(tire.needs_service())
    
    """Does not require servicing when sum of wear is below 3"""
    def test_tires_do_not_require_servicing_if_sum_of_wear_below_3(self):
        wear_array = [1, 1, 1, 0]

        tire = OctoprimeTire(wear_array)
        assertFalse(tire.needs_service())

    
if __name__ == '__main__':
    unittest.main()
