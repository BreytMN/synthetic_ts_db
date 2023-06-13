import psycopg2
from decouple import config

conn = psycopg2.connect(
    database=config("POSTGRES_DB"),
    user=config("POSTGRES_USER"),
    password=config("POSTGRES_PASSWORD"),
    host="localhost",
    port=config("POSTGRES_PORT"),
)
cur = conn.cursor()
cur.execute("SELECT * FROM timeseries")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
