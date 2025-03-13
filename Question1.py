# Define the base class Vehicle
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles

    def describe_vehicle(self):
        print(f"This vehicle is a {self.year} {self.brand} {self.model} with {self.mileage} miles.")

# Define the subclass Car
class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def describe_vehicle(self):
        super().describe_vehicle()
        print(f"It has {self.doors} doors.")

# Define the subclass Bike
class Bike(Vehicle):
    def __init__(self, brand, model, year, engine_size):
        super().__init__(brand, model, year)
        self.engine_size = engine_size

    def describe_vehicle(self):
        super().describe_vehicle()
        print(f"It has an engine size of {self.engine_size} cc.")

# Create instances of the classes
my_car = Car('Toyota', 'Corolla', 2015, 6)
my_bike = Bike('Honda', 'CRV', 2020, 125)

# Use the methods
my_car.drive(100)
my_bike.drive(50)

my_car.describe_vehicle()
my_bike.describe_vehicle()