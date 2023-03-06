import os
from dotenv import load_dotenv

BASE_PATH = os.path.dirname(os.path.abspath(__name__))

dotenv_path = os.path.join(BASE_PATH, ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")


DB = os.path.join(BASE_PATH, "events_dict.json")
AGENTS_FILE = os.path.join(BASE_PATH, "user_agents.txt")
FILE_NAME = os.path.join(BASE_PATH, "raw_data.txt")

LOGGING_FORMAT = "%(asctime)s | (line: %(lineno)s) %(levelname)s: %(message)s"
DATE_FORMAT = "%Y-%m-%d"
PAGE_URL = "https://astronomy.com/observing/sky-this-week"
IMAGE_OF_THE_DAY_URL = "https://api.nasa.gov/planetary/apod?api_key=fXQ5MaFBHMZP7oiG4usDKm9ZgcR1Brl06LmAOyts"
