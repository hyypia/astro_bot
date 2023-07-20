import re
import requests
import random
import logging
from requests.exceptions import Timeout, HTTPError
import bs4

from astro_bot.config import PAGE_URL, AGENTS


def generate_user_agents() -> dict:
    headers = {}
    try:
        with open(AGENTS, "rt") as file:
            user_agents = file.read().splitlines()
    except FileNotFoundError as fnf_err:
        logging.exception(fnf_err)
    else:
        random_user_agent = random.choice(user_agents)
        headers = {"user-agent": random_user_agent}

    return headers


def get_response(url: str) -> requests.Response:
    try:
        r = requests.get(url, headers=generate_user_agents())
        logging.info(r.status_code)
    except Timeout:
        logging.exception("The request is TIME OUT")
    except HTTPError as http_err:
        logging.exception(f"HTTP error: {http_err}")
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
