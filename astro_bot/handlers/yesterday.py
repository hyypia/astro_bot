import re
from datetime import date, timedelta

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from astro_bot.config import DATE_FORMAT
from astro_bot.handlers.get_specific_date_event import get_message_for_user


async def get_yesterday(message: types.Message) -> None:
    dt_yesterday = date.today() - timedelta(days=1)
    yesterday = re.sub(r"\b0(\d)\b", r"\1", dt_yesterday.strftime(DATE_FORMAT))
    msg = get_message_for_user(yesterday)

    await message.reply(msg)


def register_handler_yesterday(dp: Dispatcher) -> None:
    dp.register_message_handler(get_yesterday, Text(equals="Yesterday"))
