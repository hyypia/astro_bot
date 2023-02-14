from string import Template
from datetime import date, datetime, timedelta

from aiogram import Dispatcher, types

from config import DATE_FORMAT
from services.events import get_events, check_new_events
from templates import MESSAGE_WITH_EVENT, NOTHING_FOUND


def get_message_for_user(target_date: str, dates: dict) -> str:
    if target_date in dates:
        return MESSAGE_WITH_EVENT(dates[target_date])
    else:
        return NOTHING_FOUND


async def get_week(message: types.Message) -> None:
    events = await get_events()
    events_list = list(events.items())

    for _, value in events_list[-7:]:
        event = MESSAGE_WITH_EVENT(value)

        await message.reply(event)


async def get_new(message: types.Message) -> None:
    new_events = await check_new_events()

    if new_events:
        for _, value in new_events.items():
            event = MESSAGE_WITH_EVENT(value)

            await message.reply(event)
    else:
        await message.reply(NOTHING_FOUND)


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


async def get_day(message: types.Message) -> None:
    # Getting user date for searching event in db
    tmpl_date = "$year-$input_date"
    input_date = Template(tmpl_date).substitute(
        year=datetime.today().year, input_date=message.text
    )
    dt_input = datetime.strptime(input_date, DATE_FORMAT)
    target_date = dt_input.date().strftime(DATE_FORMAT)

    events = await get_events()

    msg = get_message_for_user(target_date, events)

    await message.reply(msg)


def register_handler_week(dp: Dispatcher) -> None:
    dp.register_message_handler(get_week, commands="week")
    dp.register_message_handler(get_new, commands="new")
    dp.register_message_handler(get_today, commands="today")
    dp.register_message_handler(get_yesterday, commands="yesterday")
    dp.register_message_handler(get_tomorrow, commands="tomorrow")
    dp.register_message_handler(get_day)
