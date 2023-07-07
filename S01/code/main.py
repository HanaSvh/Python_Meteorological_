#Hanie Saveh & Fatemeh Jahazi

import requests

api_key="8d16687603723daf6b6e03958fe391eb"
base_url="http://api.openweathermap.org/data/2.5/weather?q="
cityName=input("Enter city name:")
url=base_url + cityName + "&appid=" + api_key
#print(url)

result = requests.get(url)
data = result.json()
#print(data)
if data["cod"] == "404":
    print("city not found")
else:
    a=data["main"]
    #print(a)

    t=a["temp"]
    tc = t - 273.15
    print(str(round(tc,2)) + " c")
    #print(int(tc))

    p=a["pressure"]
    print(str(p) + " hpa")

    h=a["humidity"]
    print(str(h)+" %")

    w=data["weather"]
    #print(w)
    d=w[0]["description"]
    print(d)






