import logging
import asyncio
from sqlite3 import Error
from aiogram import Bot

from services.events import write_events
from services.users import get_users_ids
from handlers.week import get_week_msg_text


async def get_new_events_every_week(bot: Bot) -> None:
    while True:
        try:
            write_events()
        except Error as err:
            logging.error(err)
        else:
            users_ids = get_users_ids()
            for user_id in users_ids:
                await get_week_msg_text(bot, user_id)

        await asyncio.sleep(600)
