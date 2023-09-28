import sqlite3
from sqlite3 import Error
import os


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file, check_same_thread=False)
        print(sqlite3.version)
    except Error as e:
        print(e)
    
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


if __name__ == '__main__':
    create_connection(os.getenv('DATABASE_PATH'))
