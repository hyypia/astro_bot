import scrap_data as sd
import parse_data as pd
from astro_bot_v2.config import DB
from astro_bot_v2.db_queries import create_event_ins
from astro_bot_v2.db import write_into_db, read_from_db


def extract_data() -> dict:
    data = sd.get_data()
    data_dict = pd.parse_scraped_data_to_dict(data)
    return data_dict


def write_events() -> None:
    dates = extract_data()
    for date in dates:
        write_into_db(DB, create_event_ins, (date, dates[date]))


def main():
    write_events()


if __name__ == "__main__":
    main()
