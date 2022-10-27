
# this is the "app/unemployment_report.py" file...

import os
import json
from pprint import pprint
from statistics import mean

import requests

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)
#print(type(parsed_response))
#pprint(parsed_response)

# Challenge A
#
# What is the most recent unemployment rate? And the corresponding date?
# Display the unemployment rate using a percent sign.

#breakpoint()

latest = parsed_response["data"]

print("-------------------------")
print("LATEST UNEMPLOYMENT RATE:")
print(f"{latest[0]['value']}%", "as of", latest[0]["date"])
#print(latest)


# Challenge B
# 
# What is the average unemployment rate for all months during this calendar year?
# ... How many months does this cover?

this_year = [d for d in latest if "2022-" in d["date"]]

rates_this_year = [float(d["value"]) for d in this_year]
#print(rates_this_year)

print("-------------------------")
print("AVG UNEMPLOYMENT THIS YEAR:", f"{mean(rates_this_year)}%")
print("NO MONTHS:", len(this_year))