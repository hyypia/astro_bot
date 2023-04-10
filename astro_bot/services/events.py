"""Reading and writing data from/to db"""

import db
import queries
from config import BOOFER_FILE, DB
from services.scraper import scrap_content_to_text
from services.parse_data import cut_content, make_events_dict


async def get_data_dict() -> dict:
    content = await scrap_content_to_text()
    with open(BOOFER_FILE, "wt") as file:
        file.writelines(content)
        f_name = file.name
    content_list = cut_content(f_name)

    return make_events_dict(content_list)


async def get_events(count=None, date=None) -> list | None:
    if date:
        print(queries.select_certain_event(date))
        return await db.read_from_db(queries.select_certain_event(date), count)
    else:
        return await db.read_from_db(queries.select_events, count)


async def db_init() -> None:
    conn = db.create_connection(DB)
    if conn:
        db.execute_query(conn, queries.create_events_table)
        db.execute_query(conn, queries.create_users_table)
        print("DB inited successfully")

    dates = await get_data_dict()
    for date in dates:
        await db.write_to_db(
            queries.create_event_ins, (date,) + tuple(dates[date].values())
        )


# async def check_new_events() -> dict | None:
#     dates = await get_data_dict()
#     for date in dates:
#         await write_to_db(
#             queries.create_event_ins, (date,) + tuple(dates[date].values())
#         )
