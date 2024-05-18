from django.shortcuts import render
# Import json to load json data to python dictionary
import json
# urllib request to make a request to api
import urllib.request
from weather.settings import WEATHER_API_KEY

def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        city_data = urllib.request.urlopen(
            f"http://api.openweathermap.org/geo/1.0/direct?q={city.title()}&limit=5&appid={WEATHER_API_KEY}"
        ).read()
        city_data = json.loads(city_data)
        lon, lat = city_data[0]["lat"], city_data[0]["lon"]
        print(city_data)
        
        source = urllib.request.urlopen(
            f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}"
        ).read()

        list_of_data = json.loads(source)
        print(list_of_data)

        data = {
            "country_code": str(city_data[0]['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' 
                + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data["main"]["pressure"]),
            "humidity": str(list_of_data["main"]["humidity"]),
            "city": str(city_data[0]['name'])
        }
        print(data)
    else:
        data = {}
    return render(request, "main/index.html", data)

