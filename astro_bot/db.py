import logging
import sqlite3
from sqlite3 import Error

import queries
from config import DB


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


async def write_to_db(query: str, data: tuple) -> None:
    conn = create_connection(DB)
    if conn:
        execute_query(conn, query, data)
        conn.close()


async def read_from_db(query: str, count) -> list | None:
    conn = create_connection(DB)
    data = None
    if conn:
        data = execute_read_query(conn, query, count)
        conn.close()

    return data


def main() -> None:
    database = r"astrobase.db"

    conn = create_connection(database)
    if conn:
        print(
            execute_read_query(conn, queries.select_certain_event("2023-04-10"), None)
        )


if __name__ == "__main__":
    main()
