import unittest
import requests

from astro_bot.config import PAGE_URL
from astro_bot.services.scraper import get_url, scrap_content_to_text


class TestScraper(unittest.TestCase):
    def test_getting_url(self) -> None:
        response = requests.get(PAGE_URL)
        self.assertEqual(response.status_code, 200)
        url = get_url()
        self.assertEqual(
            url,
            "https://www.astronomy.com/observing/the-sky-this-week-welcome-summer-2/",
        )

    def test_scraping_content_page_to_text(self) -> None:
        content = scrap_content_to_text()
        self.assertEqual(content, "")


if __name__ == "__main__":
    unittest.main()
