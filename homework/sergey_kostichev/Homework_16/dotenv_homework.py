import mysql.connector as mysql
import credentials
import os
import dotenv

dotenv.load_dotenv()

print(os.getenv('DB_USER'), os.getenv('DB_PASSW'))

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()
cursor.execute("SELECT * FROM students WHERE group_id = 1981")
print(cursor.fetchall())

db.close()