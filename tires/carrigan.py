from .tire import Tire

class CarriganTire(Tire):
    def __init__(self, wear_array):
        self.wear_array = wear_array
        
    def needs_service(self):
        # Only return True if there is some value over 0.9
        for tire_wear in self.wear_array:
            if tire_wear >= 0.9:
                return True
            
        return False