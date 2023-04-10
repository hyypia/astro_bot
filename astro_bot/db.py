import logging
import sqlite3
from sqlite3 import Error

from config import DB


def create_connection(db):
    connection = None
    try:
        connection = sqlite3.connect(db)
    except Error as e:
        logging.error(e)
    finally:
        return connection


def execute_query(connection: sqlite3.Connection, query: str, params=()) -> None:
    curs = connection.cursor()
    try:
        curs.execute(query, params)
        connection.commit()
    except Error as e:
        logging.error(e)


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
