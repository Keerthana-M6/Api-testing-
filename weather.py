import requests
from pprint import pprint
url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
res = requests.get(url).json()
data = res.json()
print(res)
print(data)
pprint(data)

temp = data['main']['temp']
wind_speed = data['wind']['speed']

description = data ['weather'][0]['description']

if((id(list[]))==500)
    description = data ['weather']['description']
    print(description)

if((id(list[]))==800)
    description = data ['weather']['description']
    print(description)

print('Temperature :', temp)
print('Wind speed : {}'.format(wind_speed))
print('Description:{}'.format(description))
