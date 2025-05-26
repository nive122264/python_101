import pandas as pd

def get_city_history(city_name, df):
    city_df = df[df["City"] == city_name]
    return city_df
