import ipapi
import requests
import json 
#get the location 
ipapi.location(ip=None, key=None, field=None)
a= ipapi.location(None,None,'city')
key = '75479d19a2eca944f49dfbf0cdaadd8b'
#get current weather and load data
response = requests.get('http://api.openweathermap.org/data/2.5/weather?q={a}&APPID={key}'.format(a=a,key=key))
data = response.json()['main']
#sort jsonfile 
feels_like =str(data['feels_like'])
humid= str(data['humidity'])
cur_temp =str(data['temp'])
temp_max=str(data['temp_max'])
temp_min= str(data['temp_min'])

print(feels_like,humid,cur_temp,temp_max,temp_min) 



#Print out result 

