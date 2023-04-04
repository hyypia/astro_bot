import asyncio
import logging
import sqlite3
from sqlite3 import Error


def create_connection(db):
    conn = None
    try:
        conn = sqlite3.connect(db)
        print(f"Connection to DB successful: {sqlite3.version}")
    except Error as e:
        logging.error(e)
        print("Error: {e}")

    return conn


def execute_query(connection, query):
    curs = connection.cursor()
    try:
        curs.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        logging.error(e)
        print("Execute ERROR: {e}")


def main() -> None:
    database = r"astrobase.db"

    create_users_table = """CREATE TABLE IF NOT EXISTS users (
    telegram_id BIGINT PRIMARY KEY,
    user_name TEXT NOT NULL,
    name TEXT,
    timezone TEXT NOT NULL
    )"""

    create_events_table = """CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    iso_date TEXT NOT NULL,
    date TEXT NOT NULL,
    week_num INTEGER,
    description TEXT NOT NULL
    )"""

    conn = create_connection(database)
    execute_query(conn, create_users_table)
    execute_query(conn, create_events_table)


if __name__ == "__main__":
    main()
