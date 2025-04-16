# # 1
# import psycopg2
# import pandas as pd

# conn = psycopg2.connect("dbname='dars' user='postgres' host='localhost' password='onamotam'")
# cur = conn.cursor()

# try:
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS mock_data (
#             id INT, 
#             first_name VARCHAR(50), 
#             last_name VARCHAR(50), 
#             email VARCHAR(50), 
#             gender VARCHAR(50), 
#             ip_address VARCHAR(50)
#         );
#     """)
#     conn.commit()
#     print("Table created successfully")
# except Exception as e:
#     print("Error creating table:", e)

# df = pd.read_csv('MOCK_DATA.csv')

# for _, row in df.iterrows():
#     try:
#         cur.execute("""
#             INSERT INTO mock_data (id, first_name, last_name, email, gender, ip_address) 
#             VALUES (%s, %s, %s, %s, %s, %s);
#         """, (row['id'], row['first_name'], row['last_name'], row['email'], row['gender'], row['ip_address']))
#         conn.commit()
#         print(f"Row inserted: {row['id']}, {row['first_name']}")
#     except Exception as e:
#         print("Error inserting row:", e)

# conn.close()



# 2
def save(somsa: str):
    with open('new_data.csv', 'w+') as file:
        file.write(somsa)

save('somsa\n')
