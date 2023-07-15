import sqlite3 as sq3
from sqlite3 import Error

from services.extractor import extract_data
from db_queries import select_events, select_certain_event


DB = "astrobase.db"


def create_connection(db: str) -> sq3.Connection:
    try:
        connection = sq3.connect(db)
    except Error as err:
        print(f"DB Connection Error: {err}")
    finally:
        return connection


def execute_query(conn: sq3.Connection, sql: str, params=()) -> None:
    cursor = conn.cursor()
    try:
        cursor.execute(sql, params)
        conn.commit()
    except Error as err:
        print(f"DB Execure Query Error: {err}")


def execute_read(conn: sq3.Connection, sql: str, count) -> list | tuple:
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        if count:
            result = cursor.fetchmany(count)
        else:
            result = cursor.fetchone()
    except Error as err:
        print(f"DB Read Error: {err}")
    finally:
        return result


def db_init(db: str, sql: str) -> None:
    conn = create_connection(db)
    if conn:
        execute_query(conn, sql)
        print("DB inited successfylly")


def write_into_db(db: str, sql: str, data: tuple) -> None:
    conn = create_connection(db)
    if conn:
        execute_query(conn, sql, data)
        conn.close()


def read_from_db(db: str, sql: str, count=None) -> list | None:
    conn = create_connection(db)
    if conn:
        data = execute_read(conn, sql, count)
        conn.close()
        return data
    else:
        return None


if __name__ == "__main__":
    print(read_from_db(DB, select_certain_event("Thursday, July 20")))
