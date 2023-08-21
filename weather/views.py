from django.shortcuts import render
import json 
import urllib.request
from urllib.error import HTTPError
from urllib.parse import quote


# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city'].strip()
        try:
            encoded_city = quote(city)
            url = f'http://api.openweathermap.org/data/2.5/weather?q={encoded_city}&appid=c0e5141965e9ecde18056695ba0f69bf'
            res = urllib.request.urlopen(url).read()
            
            #res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=c0e5141965e9ecde18056695ba0f69bf').read()
            
            json_data = json.loads(res)
            data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            }
        except HTTPError as e:
            data = { "error_message": "Error: Ciudad no encontrada." }
    else:
        city = ''
        data = {}
        
    return render(request, 'index.html', {'city': city, 'data': data})