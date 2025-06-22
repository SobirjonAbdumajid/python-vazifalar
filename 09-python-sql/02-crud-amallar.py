import psycopg2

# PostgreSQL ma'lumotlar bazasiga ulanish
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="kurs_db",
    user="postgres",
    password="123"
)

# So‘rov yuborish uchun cursor
cur = conn.cursor()

# # Insert a new record
# cur.execute("INSERT INTO talabalar (ism, yosh) VALUES (%s, %s);", ("Ali", 20))
# # Insert multiple records
# cur.executemany("INSERT INTO talabalar (ism, yosh) VALUES (%s, %s);", [
#     ("Vali", 22),
#     ("Soli", 21),
#     ("Guli", 19)
# ])
#
# # INSERT/UPDATE/DELETE uchun commit qilish shart

# Ma'lumotlarni tanlash
cur.execute("SELECT * FROM talabalar;")

# Natijalarni olish
rows = cur.fetchall()

# Natijalarni konsolga chiqarish
print("\nTalabalar:")
for row in rows:
    print(row)

# Agar ma'lumotlarni yangilash kerak bo'lsa
cur.execute("UPDATE talabalar SET yosh = %s WHERE ism = %s;", (23, "Ali"))

# Agar ma'lumotlarni o'chirish kerak bo'lsa
cur.execute("DELETE FROM talabalar WHERE ism = %s;", ("Soli",))

conn.commit()

cur.execute("SELECT * FROM talabalar;")
print("\nTalabalar:")
for row in cur.fetchall():
    print(row)

# Cursor va connection’ni yopamiz
cur.close()
conn.close()