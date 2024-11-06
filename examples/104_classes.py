class Car:

    def __init__(self, name: str, weight: float = 1000) -> None:
        self.name = name
        self.weight = weight

    def add_cargo(self, cargo_kg: float) -> None:
        self.weight = self.weight + cargo_kg

    def __str__(self) -> str:
        return f"Class Car [{self.name}] {self.weight}"


jevs_car = Car("jev")
jelles_car = Car("jelle", 2500)

print(jevs_car.name, jevs_car.weight)
print(jelles_car)


for idx in range(10):
    jevs_car.add_cargo(100)
    print(jevs_car)


