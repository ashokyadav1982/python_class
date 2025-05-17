import psycopg2
from DAL.config import Config

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            dbname=Config.DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD
        )
        self.conn.autocommit = True
    
    def get_cursor(self):
        return self.conn.cursor()
    
    def close(self):
        if self.conn:
            self.conn.close()