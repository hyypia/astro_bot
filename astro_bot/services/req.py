import random
import requests
from requests.exceptions import Timeout, HTTPError

from config import AGENTS_FILE


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
