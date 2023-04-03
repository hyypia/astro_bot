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
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        logging.error(e)
        print("Execute ERROR: {e}")


def main() -> None:
    database = r"astrobase.db"
    connection = create_connection(database)
