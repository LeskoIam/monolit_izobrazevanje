# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.
import requests
import time

city = "Ljubljana"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ad5210298c8369fba090781a076f0f18&units=metric"

data = requests.get(url=url)

print(dir(data))

data = data.json()

print(data["main"]["temp"])

print(data["sys"]["sunrise"])
print(data["sys"]["sunset"])


t_rise = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(int(data["sys"]["sunrise"])))
t_set = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(int(data["sys"]["sunset"])))
print(t_rise)
print(t_set)
