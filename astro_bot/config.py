import os
from dotenv import load_dotenv

BASE_PATH = os.path.dirname(os.path.abspath(__name__))

dotenv_path = os.path.join(BASE_PATH, ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# Tokens
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
NASA_TOKEN = os.getenv("NASA_IMAGE_OF_THE_DAY_TOKEN", "")

# DBs
USERS = os.path.join(BASE_PATH, os.getenv("USERS_DB", ""))
EVENTS = os.path.join(BASE_PATH, os.getenv("EVENTS_DB", ""))
AGENTS = os.path.join(BASE_PATH, os.getenv("AGENTS_DB", ""))
BOOFER_FILE = os.path.join(BASE_PATH, os.getenv("FILE_NAME", ""))

# Formats
LOGGING_FORMAT = "%(asctime)s | (line: %(lineno)s) %(levelname)s: %(message)s"
DATE_FORMAT = "%Y-%m-%d"

# URLs
PAGE_URL = "https://astronomy.com/observing/sky-this-week"
IMAGE_OF_THE_DAY_URL = f"https://api.nasa.gov/planetary/apod?api_key={NASA_TOKEN}"
