import pytest
import requests
from bs4 import element
import sqlite3 as sq3

import config
from services import scrap_data, parse_data


class TestScraper:
    def test_page_response(self) -> None:
        res = scrap_data.get_response(config.PAGE_URL)
        assert res.status_code == requests.codes.ok, "Bad response"

    def test_get_page_content(self) -> None:
        content = scrap_data.get_content(config.PAGE_URL, "a")
        assert type(content) is element.ResultSet

    def test_get_link_for_last_week(self) -> None:
        link = scrap_data.get_link()
        assert link.startswith("https://www.astronomy.com/observing/the-sky-this-week-")

    def test_get_data_for_week(self) -> None:
        data = scrap_data.get_data()
        assert type(data) is str
        assert len(data) > 1000


# @pytest.mark.skip
class TestParser:
    def test_parse_scraped_data_to_dict(self) -> None:
        data = scrap_data.get_data()
        data_dict = parse_data.parse_scraped_data_to_dict(data)
        assert type(data_dict) is dict and len(data_dict) == 8


class TestDatabaseCRUD:
    @pytest.fixture(scope="module")
    def connection(self) -> None:
        conn = sq3.connect(":memory:")
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS 
            events (
            date TEXT NOT NULL PRIMARY KEY,
            description TEXT
        )"""
        )
        yield conn
        conn.close()

    # Insert data to table
    def test_create(self, connection) -> None:
        date = "Friday, 14"
        description = "Sunny"
        conn = connection
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO events (date, description)
                       VALUES (?, ?)""",
            (date, description),
        )
        conn.commit()
        # Checking that data was inserted successfully
        cursor.execute("SELECT * FROM events WHERE date=?", (date,))
        result = cursor.fetchone()
        assert result is not None
        assert result[0] == date
        assert result[1] == description
