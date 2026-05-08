import pandas as pd
import pymysql
import os

print("Starting MySQL load...")

connection = pymysql.connect(
    host="host.docker.internal",
    user="root",
    password="usaid123",
    database="week3_db")

cursor = connection.cursor()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
processed_path = os.path.join(PROJECT_ROOT, "data", "processed", "cleaned_api_data.csv")
df = pd.read_csv(processed_path)
print("Data loaded.")

cursor.execute("""
CREATE TABLE IF NOT EXISTS api_data (
    userId INT,
    id INT,
    title TEXT,
    body TEXT,
    title_length INT
)
""")
cursor.execute("TRUNCATE TABLE api_data")
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO api_data (userId, id, title, body, title_length)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        int(row['userId']),
        int(row['id']),
        row['title'],
        row['body'],
        int(row['title_length'])
    ))
connection.commit()
print("Data loaded into MySQL successfully.")

cursor.close()
connection.close()
