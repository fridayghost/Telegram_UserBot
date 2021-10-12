import requests

def getweather(city):
    url = f"https://openweathermap.org/data/2.5/find?q={city}&appid=439d4b804bc8187953eb36d2a8c26a02&units=metric"

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
    r = requests.get(url, headers = headers)

    jsondata = r.json()

    temp_list = []
    if len(jsondata["list"]) != 0:
        for result in jsondata["list"]:
            name = "**" + result["name"] + ", " + result["sys"]["country"] + "**"
            temp_current = "Current Temp : " + str(result["main"]["temp"] - 273.15)[:5]
            temp_feelslike = "Feels Like : " + str(result["main"]["feels_like"] - 273.15)[:5]
            temp_max = "Max Temp : " + str(result["main"]["temp_max"] - 273.15)[:5]
            humidity = "Humidity : " + str(result["main"]["humidity"])
            clouds = "Clouds : " + str(result["weather"][0]["description"])

            temp_list.append(name + "\n" + temp_current + "\n" + temp_feelslike + "\n" + temp_max + "\n" + humidity + "\n" + clouds)
    else:
        temp_list.append("Invalid entry.")

    return "\n\n".join(temp_list)