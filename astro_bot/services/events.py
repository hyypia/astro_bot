"""Reading and writing data from/to db"""

import json

from config import BOOFER_FILE, EVENTS
from services.scraper import scrap_content_to_text
from services.parse_data import cut_content, make_events_dict


async def write_to_db(data: dict) -> None:
    with open(EVENTS, "w") as db:
        json.dump(data, db, ensure_ascii=False, indent="\t")


async def read_from_db(db_name: str):
    with open(db_name, "r") as db:
        data = json.load(db)

    return data


async def get_data() -> dict:
    content = await scrap_content_to_text()

    with open(BOOFER_FILE, "wt") as file:
        file.writelines(content)
        f_name = file.name

    content_list = cut_content(f_name)

    return make_events_dict(content_list)


async def get_events():
    events = await read_from_db(EVENTS)
    return events


async def db_init() -> None:
    # events = await get_data()
    await write_to_db(await get_data())


async def check_new_events() -> dict:
    events_dict = await read_from_db(EVENTS)

    dates = await get_data()

    if dates:
        new_events = {date: dates[date] for date in dates if date not in events_dict}
        events_dict.update(new_events)

    await write_to_db(events_dict)

    return new_events
