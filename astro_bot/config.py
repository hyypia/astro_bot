import os
from dotenv import load_dotenv


load_dotenv()


TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
print(TOKEN)

BASE_PATH = os.path.dirname(__name__)
DB = os.path.join(BASE_PATH, "events_dict.json")
AGENTS_FILE = os.path.join(BASE_PATH, "user_agents.txt")
FILE_NAME = os.path.join(BASE_PATH, "digest.txt")

DATE_FORMAT = "%Y-%m-%d"
PAGE_URL = "https://astronomy.com/observing/sky-this-week"
