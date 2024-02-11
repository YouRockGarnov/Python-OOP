class TemperatureConverter:
    def celsius_to_fahrenheit(self, celsius):
        raise NotImplementedError

    def fahrenheit_to_celsius(self, fahrenheit):
        raise NotImplementedError


class InvalidTemperatureError(Exception):
    pass
