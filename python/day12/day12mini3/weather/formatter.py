
from datetime import datetime

def format_weather(data):
    """Format weather data for display"""
    if "error" in data:
        return f"Error: {data['error']}"

    city = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"].capitalize()
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted = (
        f"\nWeather Report for {city}\n"
        f"{'-'*30}\n"
        f"Temperature : {temp}°C\n"
        f"Humidity    : {humidity}%\n"
        f"Condition   : {weather}\n"
        f"Time        : {time}\n"
    )
    return formatted
