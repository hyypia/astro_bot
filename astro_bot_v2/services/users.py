from db import write_into_db
from db_queries import create_user_ins
from config import DB


def add_user(user: dict) -> None:
    write_into_db(DB, create_user_ins, tuple(user.values()))
