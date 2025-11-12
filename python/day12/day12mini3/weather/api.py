
import requests
import json

def get_weather(city):
    """Fetch weather data from OpenWeather API"""
    api_key = "your_api_key_here" 
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "City not found or API error"}
    except Exception as e:
        return {"error": str(e)}
