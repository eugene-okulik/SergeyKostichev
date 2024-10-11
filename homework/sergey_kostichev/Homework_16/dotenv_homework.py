import mysql.connector as mysql
import credentials
import os
import dotenv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=credentials.host,
    port=credentials.port,
    database=credentials.database
)