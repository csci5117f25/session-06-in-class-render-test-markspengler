# generate the database schema
import os
import psycopg2
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

conn = psycopg2.connect(os.environ['DATABASE_URL'])

# copy of schema.sql code
with conn.cursor() as cur:
    cur.execute("""
    CREATE TABLE IF NOT EXISTS guestbook_entry (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        message TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    conn.commit()

conn.close()