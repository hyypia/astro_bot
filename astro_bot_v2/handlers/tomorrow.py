from datetime import date, timedelta

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from astro_bot_v2.config import DATE_FORMAT
from astro_bot_v2.handlers.get_specific_date_event import get_message_for_user


async def get_tomorrow(message: types.Message) -> None:
    dt_tomorrow = date.today() + timedelta(days=1)
    tomorrow = dt_tomorrow.strftime(DATE_FORMAT)
    msg = get_message_for_user(tomorrow)

    await message.reply(msg)


def register_handler_tomorrow(dp: Dispatcher) -> None:
    dp.register_message_handler(get_tomorrow, Text(equals="Tomorrow"))
