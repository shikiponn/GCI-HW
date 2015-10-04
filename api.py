# -*- coding: utf-8 -*-
import urllib.request
import json
# API source http://openweathermap.org/my

api = "APPID=ff65414903d844f584bedc88eb07b163"
# APPID=APIKEY 

url = "http://api.openweathermap.org/data/2.5/weather?"
# クエリ
# 都市名
city = "q=Tokyo,jp"
temp = "units=metric"

#callAPI and get JSON
call_url = url+city+"&"+api+"&"+temp
print(call_url)
response = urllib.request.urlopen(call_url)
str_response = response.readall().decode('utf-8')
obj = json.loads(str_response)
# print(obj)
# print("整形したJSON：")
# print(json.dumps(obj, sort_keys = True, indent = 4))
print("都市名:" , obj["name"])
print("天気:" , obj["weather"][0]["description"])
print("湿度:" , obj["main"]["humidity"])
print("湿度:" , obj["main"]["temp"])
