from vehicle_factory import USVehicleFactory, EUVehicleFactory

if __name__ == "__main__":
    vehicle_factory = USVehicleFactory()
    car = vehicle_factory.create_car("Toyota", "Corolla")
    car.start_engine()

    motorcycle = vehicle_factory.create_motorcycle("Harley-Davidson", "Sportster")
    motorcycle.start_engine()

    vehicle_factory = EUVehicleFactory()
    car = vehicle_factory.create_car("Toyota", "Corolla")
    car.start_engine()

    motorcycle = vehicle_factory.create_motorcycle("Harley-Davidson", "Sportster")
    motorcycle.start_engine()
