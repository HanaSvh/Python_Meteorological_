import tkinter as tkp
import requests

api_key="8d16687603723daf6b6e03958fe391eb"
base_url="http://api.openweathermap.org/data/2.5/weather?q="

window = tkp.Tk()
window.geometry("200x200")

lblCityNotFound = tkp.Label(master=window)
lblt = tkp.Label(window)
lblp = tkp.Label(window)
lblh = tkp.Label(window)
lbld = tkp.Label(window)

def send():
    cityName = txtCityName.get()
    url = base_url + cityName + "&appid=" + api_key

    result = requests.get(url)
    data = result.json()

    if data["cod"] == "404":
        lblCityNotFound.config(text="city not found")
        lblCityNotFound.pack()
    else:
        a = data["main"]

        t = a["temp"]
        tc = t - 273.15

        p = a["pressure"]

        h = a["humidity"]

        w = data["weather"]
        d = w[0]["description"]

        lblt.config(text="temp= " + str(round(tc, 2)) + " c")
        lblp.config(text="pressure= " + str(p) + " hpa")
        lblh.config(text="humidity= " + str(h) + " %")
        lbld.config(text=d)

        lblt.pack()
        lblp.pack()
        lblh.pack()
        lbld.pack()

lblCity = tkp.Label(master=window,text="لطفا نام شهر را وارد نمایید")
txtCityName = tkp.Entry()
btnSend = tkp.Button(master=window,text="دریافت",command=send)

#widgtet
lblCity.pack()
txtCityName.pack()
btnSend.pack()

window.mainloop()