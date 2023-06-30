import pytest
import requests
from bs4 import element

import scrap_data


PAGE_URL = "https://astronomy.com/tags/sky-this-week"


class TestScraper:
    def test_page_response(self) -> None:
        res = scrap_data.get_response(PAGE_URL)
        assert res.status_code == requests.codes.ok, "Bad response"

    def test_get_page_content(self) -> None:
        content = scrap_data.get_content(PAGE_URL, "a")
        assert type(content) is element.ResultSet

    def test_get_link_for_last_week(self) -> None:
        link = scrap_data.get_link()
        assert link.startswith("https://www.astronomy.com/observing/the-sky-this-week-")

    def test_get_data_for_week(self) -> None:
        data = scrap_data.get_data()
        assert len(data) > 1000
