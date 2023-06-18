import random
import requests
import logging
from requests.exceptions import Timeout, HTTPError

from config import AGENTS


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


def make_req(url: str):
    try:
        response = requests.get(url, timeout=5, headers=generate_user_agents())
        logging.warning(response.raise_for_status())
    except Timeout:
        logging.exception("The request is time out")
    except HTTPError as http_err:
        logging.exception(f"HTTP error: {http_err}")
    except Exception as err:
        logging.exception(f"Other error: {err}")
    else:
        return response
