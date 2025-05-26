# app.py
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from fetch_realtime import get_nws_weather
from fetch_history import get_historical_weather

# Load city coordinates
cities = pd.read_csv("city_coords.csv")

# Get real-time weather for all cities
cities['Temperature'] = cities.apply(lambda row: get_nws_weather(row.Latitude, row.Longitude)['temperature'], axis=1)
cities['Summary'] = cities.apply(lambda row: get_nws_weather(row.Latitude, row.Longitude)['summary'], axis=1)

app = dash.Dash(__name__)
app.title = "USA Weather Map"

fig = px.scatter_mapbox(
    cities,
    lat="Latitude",
    lon="Longitude",
    hover_name="City",
    hover_data=["Temperature", "Summary"],
    zoom=3,
    height=600,
    color_discrete_sequence=["cyan"]
)

fig.update_layout(
    mapbox_style="carto-darkmatter",
    paper_bgcolor="#111111",
    plot_bgcolor="#111111",
    font_color="white",
    margin={"r":0, "t":0, "l":0, "b":0}
)

app.layout = html.Div([
    html.H1("USA Weather Dashboard", style={'textAlign': 'center', 'color': 'white'}),
    dcc.Graph(id="weather_map", figure=fig),
    html.Div(id='city_graph', style={"backgroundColor": "#111111", "color": "white", "padding": "10px"})
], style={"backgroundColor": "#111111", "color": "white", "minHeight": "100vh"})

@app.callback(
    Output('city_graph', 'children'),
    Input('weather_map', 'clickData')
)
def show_historical(clickData):
    if clickData:
        city = clickData['points'][0]['hovertext']
        row = cities[cities['City'] == city].iloc[0]
        hist = get_historical_weather(row.Latitude, row.Longitude)

        fig = px.line(hist, x="time", y="tavg", title=f"{city} - Temperature Last 12 Months", color_discrete_sequence=["cyan"])
        fig.update_layout(
            paper_bgcolor="#111111",
            plot_bgcolor="#111111",
            font_color="white"
        )
        return dcc.Graph(figure=fig)
    return html.P("Click a city to view historical data", style={"color": "white"})

if __name__ == '__main__':
    app.run(debug=True)