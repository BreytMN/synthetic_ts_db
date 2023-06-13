import time
from datetime import datetime
from utils.parse_args import get_start_time
from postgres.postgres_connection import new_connection
from postgres.manage_tables import create_table
from postgres.values_generator import insert_historical_values, insert_new_values


if __name__ == '__main__':
    time.sleep(10)

    start_time = get_start_time()
    conn = new_connection()

    create_table(conn)
    insert_historical_values(conn, start_time, datetime.now())
    insert_new_values(conn)
