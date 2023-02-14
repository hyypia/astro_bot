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


def make_res(url: str):
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


def get_url() -> str:
    """Getting '/sky-this-week' page and finding new url for certain week"""

    page = make_res(PAGE_URL)
    if page is None:
        return ERROR_MESSAGE

    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.find_all(href=re.compile("sky-this-week"))
    if links is None:
        return ERROR_MESSAGE
    target_link = links[0]

    return f"https://astronomy.com{target_link.get('href')}"


def save_content(link: str) -> str:
    """Getting content from page and save it in file"""

    week_url = link
    page = make_res(week_url)
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


def main():
    link = get_url()

    file_name = save_content(link)
    print(file_name)
    if file_name:
        save_content(file_name)


if __name__ == "__main__":
    main()
