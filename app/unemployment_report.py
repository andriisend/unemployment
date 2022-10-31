
import os
import json
from pprint import pprint
import plotly.express as px
import pandas as pd
import requests
from dotenv import load_dotenv 
import statistics

load_dotenv()

API_KEY = os.getenv("API_KEY")

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)

print("----------------------")
print("----------------------")
print("(Challenge A)")
data = parsed_response["data"]
print(f"The most recent unemployment rate is {data[0]['value']}% on {data[0]['date']}")
print("----------------------")
print("----------------------")
