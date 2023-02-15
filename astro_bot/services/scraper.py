"""Searching astro events for week on Astronomy Magazine
(https://astronomy.com)and pushing weekly digest and daily 
events for watching sky"""

import re
import random
import requests
from requests.exceptions import Timeout, HTTPError

from bs4 import BeautifulSoup

from templates import ERROR_MESSAGE
from config import AGENTS_FILE, PAGE_URL


def generate_user_agents() -> dict:
    with open(AGENTS_FILE, "rt") as file:
        user_agents = file.read().splitlines()
        random_user_agent = random.choice(user_agents)
        headers = {"user-agent": random_user_agent}

        return headers


def make_req(url: str):
    try:
        response = requests.get(url, timeout=5, headers=generate_user_agents())
        response.raise_for_status()

    except Timeout:
        print("The request is time out")
    except HTTPError as http_err:
        print(f"HTTP error: {http_err}")
    except Exception as err:
        print(f"Other error: {err}")

    else:
        return response


async def get_url() -> str:
    """Getting '/sky-this-week' page and finding new url for certain week"""

    res = make_req(PAGE_URL)
    if res is None:
        return ERROR_MESSAGE

    soup = BeautifulSoup(res.content, "html.parser")
    links = soup.find_all(href=re.compile("sky-this-week"))
    if links is None:
        return ERROR_MESSAGE
    target_link = links[0]

    return f"https://astronomy.com{target_link.get('href')}"


async def scrap_content_to_text() -> str:
    """Getting content from page and save it in file"""

    week_url = await get_url()
    page = make_req(week_url)
    if page is None:
        return ERROR_MESSAGE

    soup = BeautifulSoup(page.content, "html.parser")
    contents = soup.find_all("div", class_="content")
    if contents is None:
        return ERROR_MESSAGE

    text = ""
    for content in contents:
        text += content.get_text().strip() + ("\n" * 2)

    return text
