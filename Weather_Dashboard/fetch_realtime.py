# fetch_realtime.py
import requests

def get_nws_weather(lat, lon):
    headers = {"User-Agent": "USA Weather Dashboard"}
    point_url = f"https://api.weather.gov/points/{lat},{lon}"

    try:
        r = requests.get(point_url, headers=headers)
        r.raise_for_status()
        forecast_url = r.json()['properties']['forecast']
        forecast = requests.get(forecast_url, headers=headers).json()

        today = forecast['properties']['periods'][0]
        return {
            "temperature": today['temperature'],
            "unit": today['temperatureUnit'],
            "summary": today['shortForecast']
        }
    except Exception as e:
        print(f"Error fetching NWS data: {e}")
        return None