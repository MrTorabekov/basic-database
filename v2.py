import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(database=os.getenv('DB_NAME'),
                        password=os.getenv('DB_PASS'),
                        user=os.getenv('DB_USER'),
                        host=os.getenv('DB_HOST'),
                        port=os.getenv('DB_PORT')
                        )

cursor = conn.cursor()
cursor.execute('''
insert into users(name,username,address) values('Diyorbek','Torabekov_08','Tashkent')
''')

conn.commit()
conn.close()
print("Success insert data")