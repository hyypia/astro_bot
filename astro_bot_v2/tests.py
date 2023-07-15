import pytest
import requests
from bs4 import element
import sqlite3 as sq3

import config
from services import scrap_data, parse_data
from db import create_connection, execute_query, execute_read
import db_queries as q


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


class TestDatabase:
    @pytest.fixture(scope="module")
    def connection(self) -> None:
        conn = create_connection(":memory:")
        execute_query(conn, q.create_events_table)
        yield conn
        conn.close()

    # Insert data to table
    def test_execute_create_read(self, connection) -> None:
        date = "Friday, 14"
        description = "Sunny"
        execute_query(
            connection,
            q.create_event_ins,
            (date, description),
        )  # Checking that data was inserted successfully
        result = execute_read(connection, q.select_certain_event(date), None)
        assert result is not None
        assert result[0] == date
        assert result[1] == description
