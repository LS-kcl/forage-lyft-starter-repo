from .tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, wear_array):
        self.wear_array = wear_array
        
    def needs_service(self):
        total_wear = 0
        for value in self.wear_array:
            total_wear += value
            
        return total_wear >= 3