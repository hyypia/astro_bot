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

DATE_FORMAT = "%Y-%m-%d"
PAGE_URL = "https://astronomy.com/observing/sky-this-week"
