from django.shortcuts import render
# Import json to load json data to python dictionary
import json
# urllib request to make a request to api
import urllib.request
import os

app_id = os.environ.get('API_KEY')

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        
        source = urllib.request.urlopen(
            'https://api.openweathermap.org/data/3.0/weather?q =' 
            + city + f'&appid = {app_id}'
        ).read()

        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' 
                + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['mian']['temp']) + 'k',
            "pressure": str(list_of_data["main"]["pressure"]),
            "humidity": str(list_of_data["main"]["humidity"])
        }
        print(data)
    else:
        data = {}
    return render(request, "main/index.html", data)
    
