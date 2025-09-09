class Vehicle:
    def start_engine(self):
        raise NotImplementedError('Subclasses should provide implementation.')
    
class Bike(Vehicle):
    def start_engine(self):
        print("Gud Gud Gud...Bike has started !")
       
class Car(Vehicle):
    def start_engine(self):
        print("Bud Bud Bud...Car has started !")
       
class Truck(Vehicle):
    def start_engine(self):
        print("Brooom Brooom...Truck has started !")

class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == 'bike':
            return Bike()
        elif vehicle_type == 'car':
            return Car()
        elif vehicle_type == 'truck':
            return Truck()
        else:
            raise ValueError('Invalid Vehicle Type !')

if __name__ == "__main__":
    user_input = input("Enter vehicle type (Bike / Car / Truck): ")
    try:
        vehicle = VehicleFactory.get_vehicle(user_input.lower())
        vehicle.start_engine()
    except ValueError as e:
        print(f"Error: {e}")