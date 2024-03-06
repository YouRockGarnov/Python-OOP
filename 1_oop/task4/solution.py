from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self) -> str:
        pass

    @abstractmethod
    def stop(self) -> str:
        pass


class Car(Vehicle):
    def start(self) -> str:
        return "Car engine started"

    def stop(self) -> str:
        return "Car engine stopped"


class Motorcycle(Vehicle):
    def start(self) -> str:
        return "Motorcycle engine started"

    def stop(self) -> str:
        return "Motorcycle engine stopped"


class Bicycle(Vehicle):
    def start(self) -> str:
        return "Bicycle started pedaling"

    def stop(self) -> str:
        return "Bicycle stopped pedaling"


def operate_vehicle(vehicle: Vehicle) -> str:
    start_message = vehicle.start()
    stop_message = vehicle.stop()
    return f"{start_message}\n{stop_message}"


if __name__ == "__main__":
    # Создание объектов для каждого типа транспортного средства
    car = Car()
    motorcycle = Motorcycle()
    bicycle = Bicycle()

    # Вызов методов start и stop для симуляции работы с разными транспортными средствами
    car_result = operate_vehicle(car)
    motorcycle_result = operate_vehicle(motorcycle)
    bicycle_result = operate_vehicle(bicycle)

    # Вывод результатов
    print(car_result)
    print(motorcycle_result)
    print(bicycle_result)
