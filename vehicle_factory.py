from abc import ABC, abstractmethod

from vehicle import Car, Motorcycle


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> "Car":
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> "Motorcycle":
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> "Car":
        return Car(make, f"{model} (US Spec)")

    def create_motorcycle(self, make: str, model: str) -> "Motorcycle":
        return Motorcycle(make, f"{model} (US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> "Car":
        return Car(make, f"{model} (EU Spec)")

    def create_motorcycle(self, make: str, model: str) -> "Motorcycle":
        return Motorcycle(make, f"{model} (EU Spec)")
