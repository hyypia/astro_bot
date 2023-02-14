"""Analyzing scraped data from file and parse it to json"""


import re
import pytz
from datetime import datetime


def cut_content(file_name: str) -> list:
    date_pattern = re.compile(r"^\w+. \w+ \d+$", re.MULTILINE)

    with open(file_name, "rt") as file:
        source = file.read()

    dates = date_pattern.findall(source)

    others_contents = date_pattern.split(source)
    events = []
    for event in others_contents:
        if event:
            event = event[: event.find("Sunrise")]
            events.append(event)

    return [dates, events]


def calc_time(event: str, from_tz: str, to_tz: str) -> str:
    """Correct time from from_tz time zone to to_tz"""

    time_pattern = re.compile(rf"\d+(:\d+)? [AP]\.M\. {from_tz}")
    fmt = "%I %p"
    fmt_m = "%I:%M %p"
    gmt_time_lst = []
    for m in time_pattern.finditer(event):
        dt_str = re.sub(r"\.", "", m.group().strip(f" {from_tz}"))
        est = pytz.timezone(f"{from_tz}")

        try:
            dt = datetime.strptime(dt_str, fmt)
        except ValueError:
            dt = datetime.strptime(dt_str, fmt_m)

        dt_est = est.localize(dt)
        dt_utc = dt_est.astimezone(pytz.utc)
        gmt_time_lst.append(f"{dt_utc.strftime(fmt_m)} {to_tz}")

    gmt_event = event
    for i in range(0, len(gmt_time_lst)):
        gmt_event = time_pattern.sub(gmt_time_lst[i], gmt_event, count=1)

    return gmt_event


def make_events_dict(raw_lst: list) -> dict:
    if len(raw_lst[0]) != len(raw_lst[1]):
        return {}

    events_dict = {}
    fmt = "%A, %B %d, %Y"
    today = datetime.today()
    week_num = today.strftime("%W")
    for i in range(len(raw_lst[0])):
        article_date = f"{raw_lst[0][i]}, {today.year}"
        event_date = datetime.strptime(article_date, fmt)
        week_num = event_date.strftime("%W")

        event = calc_time(raw_lst[1][i], "EST", "GMT")

        events_dict[event_date.date().strftime("%Y-%m-%d")] = {
            "week": week_num,
            "date": article_date,
            "event": event,
        }

    return events_dict
