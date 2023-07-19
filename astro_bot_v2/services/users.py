from db import write_into_db, read_from_db
from db_queries import create_user_ins, select_users_id
from config import DB


def add_user(user: dict) -> None:
    write_into_db(DB, create_user_ins, tuple(user.values()))


def get_users_ids() -> list:
    return read_from_db(DB, select_users_id)[0]
