import requests
import json
#json 
def fetch_data(url):
    response = requests.get(url)
    return response.text
#json->python
def deserialize_data(raw_data):
    return json.loads(raw_data)
#day
def get_data_from_key(data, key):
    return data[key]
# item calc
def get_price(prices, item):
    return prices.get(item, 0)
#calc day
def calculate_day(day_data, prices):
    total = 0

    for drink, qty in day_data["drinks"].items():
        total += qty * get_price(prices, drink)

    for dessert, qty in day_data["desserts"].items():
        total += qty * get_price(prices, dessert)

    total += day_data["tips"]

    return total
#calc whole week
def calculate_week(data, prices):
    total_week = 0

    for day in data:
        if day == "prices":
            continue

        total_week += calculate_day(data[day], prices)

    return total_week
#
URL = "https://raw.githubusercontent.com/ruslanhamidov/coffee_data/main/coffeeshop.json"

raw = fetch_data(URL)
data = deserialize_data(raw)

prices = data["prices"]

week_total = calculate_week(data, prices)

print("Total weekly earnings:", round(week_total, 2))