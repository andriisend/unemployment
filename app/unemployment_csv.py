

import os
import json
from pprint import pprint
import plotly.express as px
import pandas as pd
import requests
from dotenv import load_dotenv 
import statistics
from app.alpha import API_KEY

csv_request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&datatype=csv&apikey={API_KEY}"
from pandas import read_csv
import pandas as pd
df = read_csv(csv_request_url)
first_row = df.iloc[0]

print("----------------------")
print("----------------------")
print("(Challenge A)")
print('The most recent unemployment rate is ' + str(first_row['value']) + '% on ' + str(first_row['timestamp']))
print("----------------------")
print("----------------------")
print("(Challenge B)")
avg_list = []
calyr = df[df['timestamp'].str.contains("2022")==True]
for f in calyr['value']:
  avg_list.append(float(f))
print("Average unemployment rate for all months during this calendar year is " + str(statistics.mean(avg_list)) + "%")
print("----------------------")
print("----------------------")
print("(Challenge C)")
print("Displaying in a new browser window...")
fig = px.line(df, x='timestamp', y='value', title='Unemployment rates over time')
fig.update_layout(yaxis_ticksuffix = '%', xaxis_title = 'Date', yaxis_title = 'Unemployment rate')
fig.show()
print("----------------------")
print("----------------------")



