import os

print("Running full pipeline...")

os.system("python scripts/fetch_api_data.py")
os.system("python scripts/clean_data.py")
os.system("python scripts/load_to_mysql.py")

print("Pipeline completed successfully.")