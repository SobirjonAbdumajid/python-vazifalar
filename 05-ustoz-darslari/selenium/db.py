import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        dbname = "job_portal_db",
        user = "postgres",
        password = "123",
        host = "localhost",
        port = "5432"
    )

def create_table_if_not_exists():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id SERIAL PRIMARY KEY,
            header VARCHAR NOT NULL,
            date VARCHAR,
            image TEXT,
            description TEXT
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
