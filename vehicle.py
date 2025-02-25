from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make: str, model: str) -> None:
        self.make: str = make
        self.model: str = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str) -> None:
        self.make: str = make
        self.model: str = model

    def start_engine(self) -> None:
        print(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str) -> None:
        self.make: str = make
        self.model: str = model

    def start_engine(self) -> None:
        print(f"{self.make} {self.model}: Мотор заведено")
