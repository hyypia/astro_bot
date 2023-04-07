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


def execute_read_query(
    connection: sqlite3.Connection, query: str, count
) -> list | None:
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        if count is None:
            result = cursor.fetchall()
        else:
            result = cursor.fetchmany(count)
    except Error as e:
        logging.error(e)
        print(f"Read DB ERROR: {e}")
    finally:
        return result


def main() -> None:
    database = r"astrobase.db"

    conn = create_connection(database)
    if conn:
        print(execute_read_query(conn, queries.select_events, -7))


if __name__ == "__main__":
    main()
