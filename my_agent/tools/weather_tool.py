import requests
import os

def get_current_weather(city: str) -> dict:
    """
    Returns current weather info for a city using OpenWeatherMap API.
    Requires API key in environment variable OPENWEATHER_API_KEY.
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    print("API key:", api_key)
    if not api_key:
        return {"status": "error", "message": "Missing API key. Please set OPENWEATHER_API_KEY"}

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200:
            return {"status": "error", "message": data.get("message", "Failed to fetch weather")}

        return {
            "status": "success",
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
