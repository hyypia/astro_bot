from datetime import datetime

from aiogram.utils.markdown import hbold

from config import DATE_FORMAT


GREETING = """Hello, I'm Astrobot!

I will searching and collect
celestial events for you.

You can send me commands:
/start - start me;
/help - get this message;
/new - check new celestial events;
/week - get weekly digest;
/today - get event for today;
/yesterday - get event for yesterday;
/tomorrow - get event for tomorrow.

You can send me date in MM-DD format
for getting celestial event for certain
date.

Let's start your astro adventure!

P.S. Special thanks Astronomy Magazine for
provided data. Visit it if you want more:
https://astronomy.com/.
"""

HELP = """/help - get this message;
/new - check new celestial events;
/week - get weekly digest;
/today - get event for today;
/yesterday - get event for yesterday;
/tomorrow - get event for tomorrow.

You can send me date in DD:MM format
for getting celestial event for certain
date.
"""

BS_ERROR = "No content found."
NOTHING_FOUND = "No events found..."
ERROR_MESSAGE = "Something went wrong. Please, try later."


def MESSAGE_WITH_EVENT(value) -> str:
    return f"{hbold(value['date'])}\n{value['event']}"


def MESSAGE_WITH_IMAGE(res_dict: dict) -> tuple:
    img = res_dict["url"]
    message = (
        f"{hbold(res_dict['title'])}\n\n "
        f"{res_dict['explanation']}\n\n "
        f"Copyright: {res_dict['copyright']}"
    )

    return img, message
