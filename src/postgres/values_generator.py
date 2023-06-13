from datetime import timedelta
import random
import time


def insert_historical_values(conn, start_time, end_time):
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
