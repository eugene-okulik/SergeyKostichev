import os
import mysql.connector as mysql
import dotenv


class SQLConnection:
    def __init__(self):
        dotenv.load_dotenv(override=True)
        self.db = self.connect_to_db()
        self.cursor = self.db.cursor()

    def connect_to_db(self):
        return mysql.connect(
            user=os.getenv('DB_USER'),
            passwd=os.getenv('DB_PASSW'),
            host=os.getenv('DB_HOST'),
            port=int(os.getenv('DB_PORT')),
            database=os.getenv('DB_NAME')
        )

    def close_db(self):
        self.db.close()

    def get_connection(self):
        return self.db

    def find_by_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
