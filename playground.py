import requests

def fetch_weather(city: str) -> dict:
    response = requests.get(f"https://api.weatherapi.com/v1/current.json?key=your_api_key&q={city}")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch data"}
