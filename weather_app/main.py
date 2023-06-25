import requests


endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = ""

weather_params = {
    "lat": "YOUR LATITUDE",
    "lon": "YOUR LONGITUDE",

}

response = requests.get(endpoint, params=weather_params)