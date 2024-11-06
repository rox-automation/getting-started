class Car:

    max_weight = 1100

    def __init__(self, name: str, weight: float = 1000) -> None:
        self.name = name
        self.weight = weight

    def add_cargo(self, cargo_kg: float) -> None:
        self.weight = self.weight + cargo_kg
        if self.weight > self.max_weight:
            raise ValueError("Too much cargo!")

    def __str__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}] {self.weight}"


class Truck(Car):

    max_weight = 5000


cars = [Truck("jev"), Car("jelle", 2500)]

for car in cars:
    print(car)


jevs_car = cars[0]

try:
    for idx in range(100):
        print(idx, jevs_car.weight)
        jevs_car.add_cargo(100)
except ValueError:
    print("no more cargo please...")
