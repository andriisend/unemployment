
import os
import json
from pprint import pprint
import plotly.express as px
import pandas as pd
import requests
from dotenv import load_dotenv 
import statistics
from plotly.express import line
from app.alpha import API_KEY

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)

print(parsed_response.keys())

print("----------------------")
print("----------------------")
print("(Challenge A)")
data = parsed_response["data"]
print(f"The most recent unemployment rate is {data[0]['value']}% on {data[0]['date']}")
print("----------------------")
print("----------------------")
print("(Challenge B)")
nums = []
for m in data:
  if '2022' in m['date']:
    nums.append(float(m['value']))
print("Average unemployment rate for all months during this calendar year is: " + str(statistics.mean(nums)) + "%")
print( "This covers " + str(len(nums)) + " months")
print("----------------------")
print("----------------------")

print("(Challenge C)")
print("Displaying in a new browser window...")
print("----------------------")
print("----------------------")
dates = []
for d in data:
    dates.append(d['date'])
values = []
for v in data:
  values.append(float(v['value']))
fig = px.line(x=dates, y=values, title = 'Unemployment rates over time')
fig.update_layout(yaxis_ticksuffix = '%', xaxis_title = 'Date', yaxis_title = 'Unemployment rate')
fig.show()
