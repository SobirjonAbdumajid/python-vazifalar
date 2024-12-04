import psycopg2

conn = psycopg2.connect("dbname='dars' user='postgres' host='localhost' password='onamotam' port='5432'")
cur = conn.cursor()

cur.execute("SELECT * FROM employee")

records = cur.fetchall()
print(records)





cur.close()
conn.close()