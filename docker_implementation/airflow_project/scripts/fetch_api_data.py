import requests
import pandas as pd
import os

print("Starting API data fetch...")

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
else:
    print("API request failed")
    exit()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

raw_path = os.path.join(PROJECT_ROOT, "data", "raw", "api_data.csv")

os.makedirs(os.path.dirname(raw_path), exist_ok=True)

df.to_csv(raw_path, index=False)

print("API data saved successfully.")
