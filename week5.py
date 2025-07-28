class Vehicle:
    def move(self):
        """Base class method to be overridden by subclasses"""
        pass

class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"

class Airplane(Vehicle):
    def move(self):
        return "✈️ Flying through the sky"

class Boat(Vehicle):
    def move(self):
        return "⛵ Sailing on water"

class Bicycle(Vehicle):
    def move(self):
        return "🚴 Cycling on the bike path"

class Submarine(Vehicle):
    def move(self):
        return "🛥️ Diving under water"

def test_vehicles():
    # Create instances of each vehicle
    car = Car()
    airplane = Airplane()
    boat = Boat()
    bicycle = Bicycle()
    submarine = Submarine()
    
    # Create a list of vehicles
    vehicles = [car, airplane, boat, bicycle, submarine]
    
    # Test each vehicle's move method
    for vehicle in vehicles:
        print(vehicle.move())

if __name__ == "__main__":
    test_vehicles()