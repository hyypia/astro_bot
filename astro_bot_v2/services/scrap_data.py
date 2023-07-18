import re
import requests
from requests.exceptions import Timeout, HTTPError
import bs4

from astro_bot_v2.config import PAGE_URL


def get_response(url: str) -> requests.Response:
    try:
        r = requests.get(url)
        print(r.status_code)
    except Timeout:
        print("The request is TIME OUT")
    except HTTPError as http_err:
        print(f"HTTP error: {http_err}")
    else:
        return r


def get_content(
    url: str, tag: str, href_=None, class_name=None
) -> bs4.element.ResultSet:
    response = get_response(url)
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    markup = soup.find_all(name=tag, class_=class_name, href=href_)
    return markup


def get_link() -> str:
    links = get_content(PAGE_URL, "a", href_=re.compile("sky-this-week"))
    return links[0].get("href")


def get_data() -> str:
    data = ""
    link = get_link()
    paragraphs = get_content(link, "p")
    for p in paragraphs:
        data += p.get_text().strip() + ("\n" * 2)
    return data