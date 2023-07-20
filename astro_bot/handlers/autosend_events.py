import logging
import asyncio
from datetime import date
from sqlite3 import Error
from aiogram import Bot

from astro_bot.config import SATURDAY, SECONDS_PER_DAY
from astro_bot.services.events import write_events
from astro_bot.services.users import get_users_ids
from astro_bot.handlers.week import get_week_msg_text


async def get_new_events_every_saturday(bot: Bot) -> None:
    try:
        write_events()
    except Error as err:
        logging.error(err)
    finally:
        users_ids = get_users_ids()
        for user_id in users_ids:
            await get_week_msg_text(bot, user_id)


async def scheduler(bot: Bot) -> None:
    """Scheduler for checking events updates every saturday"""

    while True:
        weekday = date.today().weekday()
        if weekday == SATURDAY:
            await get_new_events_every_saturday(bot)

        await asyncio.sleep(SECONDS_PER_DAY)
