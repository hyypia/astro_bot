import sqlite3 as sq3
from sqlite3 import Error

from services.extractor import extract_data


DB = "users.db"
create_users_table = """CREATE TABLE IF NOT EXISTS users (
    telegram_id BIGINT PRIMARY KEY,
    user_name TEXT NOT NULL,
    name TEXT,
    timezone TEXT NOT NULL
    )"""


def create_connection(db: str) -> sq3.Connection:
    try:
        connection = sq3.connect(db)
    except Error as err:
        print(f"DB Connection Error: {err}")
    finally:
        return connection


def execute_query(conn: sq3.Connection, query: str, params=()) -> None:
    cursor = conn.cursor()
    # args = (query, *data)
    try:
        cursor.execute(query, params)
        conn.commit()
    except Error as err:
        print(f"DB Query Error: {err}")


def execute_read(conn: sq3.Connection, query: str, count=None) -> list | tuple:
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        if count:
            result = cursor.fetchmany(count)
        else:
            result = cursor.fetchone()
    except Error as err:
        print(f"DB Read Error: {err}")
    finally:
        return result


def db_init() -> None:
    conn = create_connection(DB)
    if conn:
        execute_query(conn, create_users_table)
        print("DB init successfylly")


def write_to_db(query: str, data) -> None:
    conn = create_connection(DB)
    if conn:
        execute_query(conn, query)
        conn.close()


if __name__ == "__main__":
    db_init()
