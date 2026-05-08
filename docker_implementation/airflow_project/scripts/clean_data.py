import pandas as pd
import os

print("Starting data cleaning...")

# ---------------------------
# PATH SETUP (DYNAMIC)
# ---------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

raw_path = os.path.join(PROJECT_ROOT, "data", "raw", "api_data.csv")
processed_path = os.path.join(PROJECT_ROOT, "data", "processed", "cleaned_api_data.csv")

# ---------------------------
# LOAD DATA
# ---------------------------
df = pd.read_csv(raw_path)

print("Data loaded.")

# ---------------------------
# CLEANING
# ---------------------------
df.drop_duplicates(inplace=True)
df.fillna("N/A", inplace=True)

# ---------------------------
# FEATURE ENGINEERING
# ---------------------------
df['title_length'] = df['title'].apply(len)

print("Feature engineering complete.")

# ---------------------------
# SAVE DATA
# ---------------------------
os.makedirs(os.path.dirname(processed_path), exist_ok=True)

df.to_csv(processed_path, index=False)

print("Cleaned data saved successfully.")