"""Reading and writing data from/to db"""

import json

from config import FILE_NAME, DB
from services.scraper import scrap_content_to_text
from services.parse_data import cut_content, make_events_dict


async def get_data() -> dict:
    content = await scrap_content_to_text()

    with open(FILE_NAME, "wt") as file:
        file.writelines(content)
        f_name = file.name

    content_list = cut_content(f_name)

    return make_events_dict(content_list)


async def write_to_db(data: dict) -> None:
    with open(DB, "w") as db:
        json.dump(data, db, ensure_ascii=False, indent="\t")


async def db_init() -> None:
    # events = await get_data()
    await write_to_db(await get_data())


async def check_new_events() -> dict:
    with open(DB, "r") as db:
        events_dict = json.load(db)

    dates = await get_data()

    if dates:
        new_events = {date: dates[date] for date in dates if date not in events_dict}
        events_dict.update(new_events)

    await write_to_db(events_dict)

    return new_events


async def get_events() -> dict:
    with open(DB, "r") as db:
        events = json.load(db)

    return events
