# twilio
# Api authetication
from requests import *
from twilio.rest import Client
import os
account_sid = os.getenv('sid')
auth_token = os.getenv('auth')
parameters = {
    'appid': os.getenv('api'),
    'lat': 8.3, # use your location
    'lon': -13, # use your location
    'exclude': 'current,daily'
}
weather = get('https://api.openweathermap.org/data/3.0/onecall', params=parameters)
weather.raise_for_status()
weather_data = weather.json()
hours_12 = [weather_data['hourly'][i]['weather'] for i in range(12)]
hours_12_weather = [{'id': hours_12[i][0]['id'],
                     'main': hours_12[i][0]['main'],
                     'desc': hours_12[i][0]['description']
                     } for i in range(12)]
will_rain = False
for i in hours_12_weather:
    if int(i['id']) < 700:
        main = i['main']
        desc = i['desc']
        will_rain = True
if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages \
            .create(
        body= f'There would be {main} today specifically {desc} get ready!🥷' ,
        from_= '+17055351044',
        to = '+17097250935'
    )
