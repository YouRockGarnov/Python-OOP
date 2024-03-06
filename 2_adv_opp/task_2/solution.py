class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        if not isinstance(celsius, (int, float)):
            raise InvalidTemperatureError("Input must be a number")
        return celsius * 9/5 + 32

    def fahrenheit_to_celsius(self, fahrenheit):
        if not isinstance(fahrenheit, (int, float)):
            raise InvalidTemperatureError("Input must be a number")
        return (fahrenheit - 32) * 5/9


class InvalidTemperatureError(Exception):
    pass
