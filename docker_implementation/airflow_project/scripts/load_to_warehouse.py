import pandas as pd
import psycopg2

# Load CSV
df = pd.read_csv("/opt/airflow/data/processed/cleaned_api_data.csv")


connection = psycopg2.connect(
    host="postgres",
    database="warehouse_db",
    user="admin",
    password="admin",
    port="5432"
)

cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS api_data (
    userid INTEGER,
    id INTEGER PRIMARY KEY,
    title TEXT,
    body TEXT,
    title_length INTEGER
)
""")

connection.commit()

# Insert data
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO api_data (userid, id, title, body, title_length)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        int(row['userId']),
        int(row['id']),
        row['title'],
        row['body'],
        int(row['title_length'])
    ))

connection.commit()

print("Data loaded into warehouse successfully!")

cursor.close()
connection.close()