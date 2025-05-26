# fetch_history.py
from meteostat import Point, Daily
from datetime import datetime
import pandas as pd

def get_historical_weather(lat, lon):
    today = datetime.now()
    last_year = today.replace(year=today.year - 1)
    location = Point(lat, lon)

    data = Daily(location, last_year, today)
    data = data.fetch()
    return data.reset_index()  # columns: time, tavg, tmin, tmax, prcp, snow, etc.