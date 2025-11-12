
from weather.api import get_weather
from weather.formatter import format_weather

def run():
    """CLI for the weather report app"""
    city = input("Enter city name: ")
    data = get_weather(city)
    print(format_weather(data))
