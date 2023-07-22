from astro_bot.services.extractor import extract_data
from astro_bot.db import write_into_db, read_from_db
from astro_bot.config import DB
from astro_bot.db_queries import (
    create_event_ins,
    select_certain_event,
    select_last_new_events,
)


def write_events() -> None:
    dates = extract_data()
    for date in dates:
        write_into_db(DB, create_event_ins, tuple([date, dates[date]]))


def get_events(date=None, count=None) -> list | None:
    if date:
        return read_from_db(DB, select_certain_event(date))
    if count:
        return read_from_db(DB, select_last_new_events(count))
