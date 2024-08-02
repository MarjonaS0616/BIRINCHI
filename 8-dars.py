import requests
import json

url = "https://nbu.uz/uz/exchange-rates/json/"

def send_req(url):
    base = requests.get(url)
    return base

def makeJson(base):
    madeJSON = json.loads(base.content)
    return madeJSON

def anothersum(deta:list):
    cald = deta[-11]
    return cald['nbu_buy_price']
    
    
def get_uzbeksum(data:list):
    calc = data[-1]
    return calc['nbu_buy_price']
    
def uzbek_sum(dollar:int):
    uz_sum = float(summa) * dollar
    return uz_sum

requested_data = send_req(url)
makeJS = makeJson(requested_data)
summa = get_uzbeksum(makeJS)
another = anothersum(makeJS)
uzbek_summaa = uzbek_sum(2)
print(another)


# import requests
# import json
# url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"

# def send_requ(url):
#     base = requests.get(url)
#     return base

# def madeJson(base):
#     madeLSON = json.loads(base.content)
#     return madeLSON
# def get_wether(data:list):
