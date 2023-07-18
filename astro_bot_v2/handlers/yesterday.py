from datetime import date, timedelta

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from config import DATE_FORMAT
from handlers.get_specific_date_event import get_message_for_user


async def get_yesterday(message: types.Message) -> None:
    dt_yesterday = date.today() - timedelta(days=1)
    yesterday = dt_yesterday.strftime(DATE_FORMAT)
    msg = get_message_for_user(yesterday)

    await message.reply(msg)


def register_handler_yesterday(dp: Dispatcher) -> None:
    dp.register_message_handler(get_yesterday, Text(equals="Yesterday"))
