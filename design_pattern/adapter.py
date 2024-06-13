class CelsiusTemperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature

class FahrenheitTemperatureAdapter:
    def __init__(self, celsius_temperature):
        self.celsius_temperature = celsius_temperature

    def get_temperature(self):
        return self.celsius_to_fahrenheit(self.celsius_temperature.get_temperature())

    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

# Usage
celsius_temp = CelsiusTemperature(25)
print(f"Celsius Temperature: {celsius_temp.get_temperature()} °C")  # Output: 25 °C

fahrenheit_temp_adapter = FahrenheitTemperatureAdapter(celsius_temp)
print(f"Fahrenheit Temperature: {fahrenheit_temp_adapter.get_temperature()} °F")  # Output: 77.0 °F
