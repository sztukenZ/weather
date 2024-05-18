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
        appid = 