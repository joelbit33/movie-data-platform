import psycopg
from dotenv import load_dotenv
import os
load_dotenv()  # load variables from .env file

pg_host = os.getenv('PG_HOST')
pg_port = os.getenv('PG_PORT')
pg_dbname = os.getenv('PG_DBNAME')
pg_user = os.getenv('PG_USER')
pg_password = os.getenv('PG_PASSWORD')

def database_read():
    with psycopg.connect(f"host={pg_host} port={pg_port} dbname={pg_dbname} user={pg_user} password={pg_password}") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM movies_base LIMIT 5")
            cur.fetchone()
            for record in cur:
                print("--------------")
                print(record)

database_read()