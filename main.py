import time
import random
import psycopg2
from datetime import datetime, timedelta
import argparse
import os


def get_start_time():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start-time', type=str, default=None,
                        help='Start time in format "YYYY-MM-DD HH:MM:SS"')
    args = parser.parse_args()

    default_start_time = datetime.now() - timedelta(days=7)
    start_time_str = args.start_time or str(default_start_time)
    return datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')


def postgres_connect():

    return psycopg2.connect(
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
    )


def create_table(conn):
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE timeseries (
            id SERIAL PRIMARY KEY, 
            timestamp TIMESTAMP, 
            value FLOAT, 
            data_group VARCHAR(255), 
            data_subgroup VARCHAR(255)
        );
    """)
    conn.commit()


def insert_values(conn, start_time, end_time):
    cur = conn.cursor()

    # Generate random integers and timestamps within the time interval
    while start_time < end_time:
        value = random.randint(1, 100)
        cur.execute("""
            INSERT INTO timeseries (value, timestamp, data_group, data_subgroup)
            VALUES (%s, %s, 'group1', 'subgroup1');
        """, (value, start_time))
        start_time += timedelta(seconds=30)

    conn.commit()


def insert_new_values(conn):
    cur = conn.cursor()

    # Continuously insert new values with current timestamp
    while True:
        value = random.randint(1, 100)
        cur.execute("""
            INSERT INTO timeseries (value, timestamp, data_group, data_subgroup)
            VALUES (%s, now(), 'group1', 'subgroup2');
        """, (value,))
        conn.commit()
        time.sleep(10)


if __name__ == '__main__':
    time.sleep(10)

    start_time = get_start_time()
    conn = postgres_connect()

    create_table(conn)
    insert_values(conn, start_time, datetime.now())
    insert_new_values(conn)
