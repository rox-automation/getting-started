# This code demonstrates Object-Oriented Programming using classes in Python
# A class is like a blueprint that defines what properties and behaviors an object should have
# Classes help organize code and model real-world concepts


class Car:
    # Class variable shared by all instances of Car
    # Represents maximum allowed weight in kilograms
    max_weight = 1100

    def __init__(self, name: str, weight: float = 1000) -> None:
        # Constructor method that initializes a new Car object
        # Parameters:
        #   name: identifier for the car
        #   weight: starting weight in kg, defaults to 1000
        self.name = name
        self.weight = weight

    def add_cargo(self, cargo_kg: float) -> None:
        # Method to add cargo weight to the car
        # Raises ValueError if total weight exceeds max_weight
        self.weight = self.weight + cargo_kg
        if self.weight > self.max_weight:
            raise ValueError("Too much cargo!")

    def __str__(self) -> str:
        # Special method that returns string representation of the car
        # Used when printing the object
        return f"{self.__class__.__name__} [{self.name}] {self.weight}"


class Truck(Car):
    # Truck class inherits from Car class (indicated by Car in parentheses)
    # This means Truck has all Car's features but can override some values
    # Here we override max_weight to allow trucks to carry more
    max_weight = 5000


# Create a list containing two vehicles:
# 1. A Truck for Alice with default weight
# 2. A Car for Bob with custom weight of 2500kg
cars = [Truck("alice"), Car("bob", 2500)]

# Print string representation of each vehicle
for car in cars:
    print(car)


# Get reference to Alice's truck (first vehicle in list)
alices_car = cars[0]

try:
    # Attempt to add cargo in 100kg increments
    # This loop will continue until max_weight is exceeded
    for idx in range(100):
        print(idx, alices_car.weight)
        alices_car.add_cargo(100)
except ValueError:
    # When max_weight is exceeded, catch the error and print message
    print("no more cargo please...")
