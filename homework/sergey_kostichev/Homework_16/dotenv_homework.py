import mysql.connector as mysql
import credentials
import os
import dotenv

dotenv.load_dotenv()

print(os.getenv('DB_USER'), os.getenv('DB_PASSW'))
db = mysql.connect(
    user='st4',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host=credentials.host,
    port=credentials.port,
    database=credentials.database
)

cursor = db.cursor()
cursor.execute("SELECT * FROM students WHERE group_id = 1981")
print(cursor.fetchall())

db.close()