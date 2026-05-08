import pandas as pd
import psycopg2

# Load cleaned data
df = pd.read_csv("/opt/airflow/data/processed/cleaned_api_data.csv")

# Connect to PostgreSQL warehouse
connection = psycopg2.connect(
    host="host.docker.internal",
    database="warehouse_db",
    user="admin",
    password="admin",
    port="5432"
)

cursor = connection.cursor()

# Create analytics table
cursor.execute("""
CREATE TABLE IF NOT EXISTS api_data (
    id SERIAL PRIMARY KEY,
    column1 TEXT,
    column2 TEXT
)
""")

# Insert data
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO api_data (column1, column2)
        VALUES (%s, %s)
    """, (
        str(row.iloc[0]),
        str(row.iloc[1])
    ))

# Commit changes
connection.commit()

print("Data loaded into warehouse successfully!")

# Close connections
cursor.close()
connection.close()