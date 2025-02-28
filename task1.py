from vehicle_factory import USVehicleFactory, EUVehicleFactory
from logger import logger, setup_logging

setup_logging()

if __name__ == "__main__":
    vehicle_factory = USVehicleFactory()
    car = vehicle_factory.create_car("Toyota", "Corolla")
    logger.info("Creating a car")
    car.start_engine()

    motorcycle = vehicle_factory.create_motorcycle("Harley-Davidson", "Sportster")
    motorcycle.start_engine()

    vehicle_factory = EUVehicleFactory()
    car = vehicle_factory.create_car("Toyota", "Corolla")
    logger.info("Creating a car")
    car.start_engine()

    motorcycle = vehicle_factory.create_motorcycle("Harley-Davidson", "Sportster")
    motorcycle.start_engine()
