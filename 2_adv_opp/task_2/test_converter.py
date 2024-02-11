import pytest
from .converter import TemperatureConverter, InvalidTemperatureError


def test_temperature_converter():
    converter = TemperatureConverter()
    assert converter.celsius_to_fahrenheit(0) == 32
    assert converter.fahrenheit_to_celsius(32) == 0

    with pytest.raises(InvalidTemperatureError):
        converter.celsius_to_fahrenheit("invalid")
        converter.fahrenheit_to_celsius("invalid")
