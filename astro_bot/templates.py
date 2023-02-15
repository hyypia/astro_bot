from aiogram.utils.markdown import hbold


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

NOTHING_FOUND = "No events found..."


ERROR_MESSAGE = "Something went wrong. Please, try later."


def MESSAGE_WITH_EVENT(value):
    return f"{hbold(value['date'])}\n{value['event']}"
