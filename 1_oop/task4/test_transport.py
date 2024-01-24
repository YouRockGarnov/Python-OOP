import pytest
from transport import Car, Motorcycle, Bicycle, operate_vehicle


def test_operate_vehicle_car():
    car = Car()
    try:
        result = operate_vehicle(car)
    except Exception as e:
        pytest.fail(f"operate_vehicle raised an exception: {e}")

def test_operate_vehicle_motorcycle():
    motorcycle = Motorcycle()
    try:
        result = operate_vehicle(motorcycle)
    except Exception as e:
        pytest.fail(f"operate_vehicle raised an exception: {e}")

def test_operate_vehicle_bicycle():
    bicycle = Bicycle()
    try:
        result = operate_vehicle(bicycle)
    except Exception as e:
        pytest.fail(f"operate_vehicle raised an exception: {e}")
