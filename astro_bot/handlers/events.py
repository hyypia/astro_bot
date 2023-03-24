from datetime import date, timedelta

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from config import DATE_FORMAT
from services.events import get_events
from templates import MESSAGE_WITH_EVENT, NOTHING_NEWS_FOUND


def get_message_for_user(target_date: str, dates: dict) -> str:
    if target_date in dates:
        return MESSAGE_WITH_EVENT(dates[target_date])
    else:
        return NOTHING_NEWS_FOUND


async def get_today(message: types.Message) -> None:
    today = date.today().strftime(DATE_FORMAT)
    events = await get_events()

    msg = get_message_for_user(today, events)

    await message.reply(msg)


async def get_yesterday(message: types.Message) -> None:
    dt_yesterday = date.today() - timedelta(days=1)
    yesterday = dt_yesterday.strftime(DATE_FORMAT)
    events = await get_events()

    msg = get_message_for_user(yesterday, events)

    await message.reply(msg)


async def get_tomorrow(message: types.Message) -> None:
    dt_tomorrow = date.today() + timedelta(days=1)
    tomorrow = dt_tomorrow.strftime(DATE_FORMAT)
    events = await get_events()

    msg = get_message_for_user(tomorrow, events)

    await message.reply(msg)


def register_handler_events(dp: Dispatcher):
    dp.register_message_handler(get_today, Text(equals="Today"))
    dp.register_message_handler(get_yesterday, Text(equals="Yesterday"))
    dp.register_message_handler(get_tomorrow, Text(equals="Tomorrow"))
