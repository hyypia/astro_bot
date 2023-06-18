"""Searching astro events for week on Astronomy Magazine site
(https://astronomy.com) and pushing weekly digest and daily
events for watching sky"""

import re

from bs4 import BeautifulSoup

from services.req import make_req
from templates import SCRAPING_ERROR_MESSAGE, ERROR_MESSAGE
from config import PAGE_URL


def get_url() -> str:
    """Getting '/sky-this-week' page and finding new url for certain week"""

    res = make_req(PAGE_URL)
    if res is None:
        return ERROR_MESSAGE
    soup = BeautifulSoup(res.content, "html.parser")
    links = soup.find_all("a", href=re.compile("sky-this-week"))
    if links is None:
        return SCRAPING_ERROR_MESSAGE
    target_link = links[1]

    return target_link.get("href")


def scrap_content_to_text() -> str:
    """Getting content from page and save it in file"""

    week_url = get_url()
    page = make_req(week_url)
    if page is None:
        return ERROR_MESSAGE
    soup = BeautifulSoup(page.content, "html.parser")
    contents = soup.find_all("div", class_="entry-content")
    if contents is None:
        return SCRAPING_ERROR_MESSAGE
    text = ""
    for content in contents:
        text += content.get_text().strip() + ("\n" * 2)

    return text
