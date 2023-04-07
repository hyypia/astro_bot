from aiogram.utils.markdown import hbold


GREETING_MESSAGE = f"""Hello, I'm Astrobot!

I will searching and collect celestial events for you.

If you want getting actual date and time of events for your local, please \
push {hbold("Share location")} key or {hbold("GMT")} key for getting date and \
time for GMT time zone (UTC+0).

Let's start your astro adventure!

P.S. Special thanks Astronomy Magazine for provided data. Visit \
https://astronomy.com/ if you want more.
"""

START_MESSAGE = f"""You can send me commands (press keys):

{hbold("Help")} - get message with commands list;
{hbold("New")} - check new celestial events;
{hbold("Week")} - get weekly digest;
{hbold("Today")} - get event for today;
{hbold("Yesterday")} - get event for yesterday;
{hbold("Tomorrow")} - get event for tomorrow;
{hbold("Image of the day")} - for get image of the day from NASA.

You can send me date in {hbold("MM-DD")} format for getting celestial event \
for certain date.
"""

HELP_MESSAGE = f"""{hbold("Help")} - get message with commands list;
{hbold("New")} - check new celestial events;
{hbold("Week")} - get weekly digest;
{hbold("Today")} - get event for today;
{hbold("Yesterday")} - get event for yesterday;
{hbold("Tomorrow")} - get event for tomorrow;
{hbold("Image of the day")} - for get image of the day from NASA.

You can send me date in {hbold("MM-DD")} format for getting celestial event \
for certain date.
"""

SCRAPING_ERROR_MESSAGE = "No content found."
ERROR_MESSAGE = "Something went wrong. Please, try later."
NOTHING_NEWS_FOUND = "No events found..."


def MESSAGE_WITH_EVENT(date, description) -> str:
    return f"{hbold(date)}\n{description}"


def MESSAGE_WITH_IMAGE(res_dict: dict) -> tuple:
    img = res_dict["url"]
    message = (
        f"{hbold(res_dict['title'])}\n\n"
        f"{res_dict['explanation']}\n\n"
        f"Copyright: {res_dict['copyright']}"
    )

    return img, message
