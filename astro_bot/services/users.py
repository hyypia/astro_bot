from db import write_to_db
from queries import create_user_ins


async def add_user(user: dict) -> None:
    await write_to_db(create_user_ins, tuple(user.values()))
