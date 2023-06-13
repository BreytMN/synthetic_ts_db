import psycopg2
from decouple import config


def new_connection():
    return psycopg2.connect(
        database=config("POSTGRES_DB"),
        user=config("POSTGRES_USER"),
        password=config("POSTGRES_PASSWORD"),
        host=config("POSTGRES_HOST"),
        port=config("POSTGRES_PORT"),
    )
