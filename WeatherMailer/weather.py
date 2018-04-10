import requests


def get_weather():
    url = "http://api.openweathermap.org/data/2.5/weather?q=Bellevue,us&units=imperial&appid=96669274ea5b65e65143e45f1e5dd99f"
    weather_request = requests.get(url)
    weather_json = weather_request.json()
    description = weather_json["weather"][0]["description"]
    max_temp = weather_json["main"]["temp_max"]
    min_temp = weather_json["main"]["temp_min"]
    weather = str(description).title() + " with a high of " + str(max_temp) + "F and a low of " + str(min_temp) + "F."
    return weather
