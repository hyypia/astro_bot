from datetime import date

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from astro_bot.config import DATE_FORMAT
from astro_bot.handlers.get_specific_date_event import get_message_for_user


async def get_today(message: types.Message) -> None:
    today = date.today().strftime(DATE_FORMAT)
    msg = get_message_for_user(today)

    await message.reply(msg)


def register_handler_today(dp: Dispatcher):
    dp.register_message_handler(get_today, Text(equals="Today"))
