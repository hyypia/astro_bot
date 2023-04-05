import logging
import sqlite3
from sqlite3 import Error

import queries


def create_connection(db):
    connection = None
    try:
        connection = sqlite3.connect(db)
        print(f"Connection to DB successful: {sqlite3.version}")
    except Error as e:
        logging.error(e)
        print(f"Error: {e}")
    finally:
        return connection


def execute_query(connection: sqlite3.Connection, query: str, params=()) -> None:
    curs = connection.cursor()
    try:
        curs.execute(query, params)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        logging.error(e)
        print(f"Execute ERROR: {e}")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except Error as e:
        logging.error(e)
        print(f"Read DB ERROR: {e}")
    finally:
        return result


def main() -> None:
    database = r"astrobase.db"

    conn = create_connection(database)
    execute_query(conn, queries.create_users_table)
    execute_query(conn, queries.create_events_table)


if __name__ == "__main__":
    main()
