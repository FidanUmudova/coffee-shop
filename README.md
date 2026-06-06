Coffee Shop Weekly Earnings Calculator

This project calculates the total earnings of a coffee shop for one week using sales data from a JSON file.

Project Description

The program:

Fetches data from a remote JSON URL
Converts JSON data into a Python dictionary
Processes daily sales data (drinks, desserts, tips)
Calculates daily earnings
Calculates total weekly earnings

Data Structure

The JSON file contains:

prices (price list of all items)
monday to sunday (daily sales data)
drinks
desserts
tips

Functions

fetch_data(url)
Fetches JSON data from a given URL

deserialize_data(raw_data)
Converts JSON string into Python dictionary

get_data_from_key(data, key)
Returns data for a specific day

get_price(prices, item)
Returns price of a given item

calculate_day(day_data, prices)
Calculates total earnings for one day

calculate_week(data, prices)
Calculates total earnings for the whole week

How to Run

python coffeeshop.py

Requirements

pip install requests

Output Example

Total weekly earnings: 5234.75

Data Source

https://raw.githubusercontent.com/ruslanhamidov/coffee_data/main/coffeeshop.json

What I Learned

Working with APIs
JSON parsing
Dictionaries and loops
Functions and modular programming
Real-world data calculations
