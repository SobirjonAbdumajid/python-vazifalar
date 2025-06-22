import psycopg2

try:
    # 🔌 Baza bilan ulanish
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        dbname="kurs_db",
        user="postgres",
        password="123"
    )

    # 🔁 Avtomatik commit yo‘q, biz nazorat qilamiz
    conn.autocommit = False

    cur = conn.cursor()

    # ⚙️ Transaksiyani boshlaymiz
    cur.execute("INSERT INTO talabalar (ism, yosh) VALUES (%s, %s);", ("Olim", 20))

    # 🔥 Noto‘g‘ri query — xatolik chiqarish uchun
    cur.execute("INSERT INTO talabalar (ism, yosh) VALUES ('Xato', 'not_a_number');")

    # 🧾 Agar hech qanday xatolik bo‘lmasa — commit qilamiz
    conn.commit()

except Exception as e:
    print("🚨 Xatolik yuz berdi:", e)
    conn.rollback()  # 🔙 Hamma o‘zgarishlarni bekor qilamiz

finally:
    # 🔚 Har qanday holatda ham resurslarni tozalaymiz
    if cur:
        cur.close()
    if conn:
        conn.close()
