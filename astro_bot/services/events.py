"""Reading and writing data from/to db"""

import json

import db
import queries
from config import BOOFER_FILE, EVENTS, DB
from services.scraper import scrap_content_to_text
from services.parse_data import cut_content, make_events_dict


async def write_to_db(query: str, data: tuple) -> None:
    conn = db.create_connection(DB)
    if conn:
        db.execute_query(conn, query, data)
        conn.close()


async def read_from_db(query: str, count) -> list | None:
    conn = db.create_connection(DB)
    data = None
    if conn:
        data = db.execute_read_query(conn, query, count)
        conn.close()

    return data


async def get_data_dict() -> dict:
    content = await scrap_content_to_text()
    with open(BOOFER_FILE, "wt") as file:
        file.writelines(content)
        f_name = file.name
    content_list = cut_content(f_name)

    return make_events_dict(content_list)


async def get_events(count=None) -> list | None:
    events = await read_from_db(queries.select_events, count)
    return events


async def db_init() -> None:
    conn = db.create_connection(DB)
    if conn:
        db.execute_query(conn, queries.create_events_table)
        db.execute_query(conn, queries.create_users_table)
        print("DB inited successfully")

    dates = await get_data_dict()
    for date in dates:
        await write_to_db(
            queries.create_event_ins, (date,) + tuple(dates[date].values())
        )


async def check_new_events() -> dict | None:
    pass
#     events_dict = await read_from_db(EVENTS)
#
#     dates = await get_data_dict()
#
#     if dates:
#         new_events = {date: dates[date] for date in dates if date not in events_dict}
#         events_dict.update(new_events)
#
#         # await write_to_db(events_dict)
#
#         return new_events


async def add_user(user: dict) -> None:
    await write_to_db(queries.create_user_ins, tuple(user.values()))
