import pandas as pd
import os

print("Starting data cleaning...")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

raw_path = os.path.join(PROJECT_ROOT, "data", "raw", "api_data.csv")
processed_path = os.path.join(PROJECT_ROOT, "data", "processed", "cleaned_api_data.csv")
df = pd.read_csv(raw_path)
print("Data loaded.")

df.drop_duplicates(inplace=True)
df.fillna("N/A", inplace=True)
df['title_length'] = df['title'].apply(len)
print("Feature engineering complete.")

os.makedirs(os.path.dirname(processed_path), exist_ok=True)
df.to_csv(processed_path, index=False)

print("Cleaned data saved successfully.")
