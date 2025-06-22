import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="kurs_db",
    user="postgres",
    password="123"
)

cur = conn.cursor()

# Create a table
cur.execute("""
    CREATE TABLE IF NOT EXISTS talabalar (
        id SERIAL PRIMARY KEY,
        ism VARCHAR(50),
        yosh INTEGER
    );
""")

conn.commit()
cur.close()
conn.close()
