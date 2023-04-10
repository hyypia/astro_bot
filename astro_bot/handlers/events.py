from datetime import date, timedelta

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from config import DATE_FORMAT
from services.events import get_events
from templates import MESSAGE_WITH_EVENT, NOTHING_NEWS_FOUND


async def get_message_for_user(date: str) -> str:
    row = await get_events(date=date)
    if row:
        day, event = row[0]
        return MESSAGE_WITH_EVENT(day, event)
    else:
        return NOTHING_NEWS_FOUND


async def get_today(message: types.Message) -> None:
    today = date.today().strftime(DATE_FORMAT)
    msg = await get_message_for_user(today)

    await message.reply(msg)


async def get_yesterday(message: types.Message) -> None:
    dt_yesterday = date.today() - timedelta(days=1)
    yesterday = dt_yesterday.strftime(DATE_FORMAT)
    msg = await get_message_for_user(yesterday)

    await message.reply(msg)


async def get_tomorrow(message: types.Message) -> None:
    dt_tomorrow = date.today() + timedelta(days=1)
    tomorrow = dt_tomorrow.strftime(DATE_FORMAT)
    msg = await get_message_for_user(tomorrow)

    await message.reply(msg)


def register_handler_events(dp: Dispatcher):
    dp.register_message_handler(get_today, Text(equals="Today"))
    dp.register_message_handler(get_yesterday, Text(equals="Yesterday"))
    dp.register_message_handler(get_tomorrow, Text(equals="Tomorrow"))
