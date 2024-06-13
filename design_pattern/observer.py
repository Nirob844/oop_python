from abc import ABC, abstractmethod


class Subject(ABC):
    """Subject Interface"""
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class WeatherData(Subject):
    """Concrete Subject"""
    def __init__(self):
        self._observers = []
        self._temperature = None
        self._humidity = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity)

    def set_measurements(self, temperature, humidity):
        self._temperature = temperature
        self._humidity = humidity
        self.notify()

class Observer(ABC):
    """Observer Interface"""
    @abstractmethod
    def update(self, temperature, humidity):
        pass

class CurrentConditionsDisplay(Observer):
    """Concrete Observer for Current Conditions"""
    def update(self, temperature, humidity):
        print(f"Current conditions: {temperature}°C and {humidity}% humidity")

class StatisticsDisplay(Observer):
    """Concrete Observer for Statistics"""
    def __init__(self):
        self._temperatures = []

    def update(self, temperature, humidity):
        self._temperatures.append(temperature)
        avg_temp = sum(self._temperatures) / len(self._temperatures)
        print(f"Avg/Max/Min temperature = {avg_temp:.1f}/{max(self._temperatures)}/{min(self._temperatures)}")

# Usage
weather_data = WeatherData()

current_display = CurrentConditionsDisplay()
statistics_display = StatisticsDisplay()

weather_data.attach(current_display)
weather_data.attach(statistics_display)

weather_data.set_measurements(28, 65)
# Output:
# Current conditions: 28°C and 65% humidity
# Avg/Max/Min temperature = 28.0/28/28

weather_data.set_measurements(30, 70)
# Output:
# Current conditions: 30°C and 70% humidity
# Avg/Max/Min temperature = 29.0/30/28

weather_data.set_measurements(26, 90)
# Output:
# Current conditions: 26°C and 90% humidity
# Avg/Max/Min temperature = 28.0/30/26
