import logging
import json
import asyncio
from datetime import date, datetime, timedelta
from string import Template

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold

import templates
from config import TOKEN, DB, DATE_FORMAT
from main import check_new_events, get_events


logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def start(message: types.Message) -> None:
    await message.answer(templates.GREETING)


@dp.message_handler(commands="week")
async def get_week(message: types.Message) -> None:
    #     with open(DB, "r") as file:
    #         events_dict = json.load(file)

    events = get_events()
    week = list(events.items())
    for key, value in week[-7:]:
        event: str = f"{hbold(value['date'])}\n{value['event']}"

        await message.reply(event)


@dp.message_handler(commands="new")
async def get_new(message: types.Message) -> None:
    new_events: dict = check_new_events()

    if new_events:
        for key, value in new_events.items():
            event: str = f"{hbold(value['date'])}\n{value['event']}"

            await message.answer(event)
    else:
        await message.reply(templates.NOTHING_FOUND)


@dp.message_handler(commands="today")
async def get_today(message: types.Message) -> None:
    today = date.today().strftime(DATE_FORMAT)

    events = get_events()

    if today in events:
        event = f"{hbold(events[today]['date'])}\n{events[today]['event']}"

        await message.reply(event)

    else:
        await message.reply("Nothing for today.")


@dp.message_handler(commands="yesterday")
async def get_yesterday(message: types.Message) -> None:
    dt_yesterday = date.today() - timedelta(days=1)
    yesterday = dt_yesterday.strftime(DATE_FORMAT)

    events = get_events()

    if yesterday in events:
        event = f"{hbold(events[yesterday]['date'])}\n\
            {events[yesterday]['event']}"

        await message.reply(event)

    else:
        await message.reply("There was nothing yesterday.")


@dp.message_handler(commands="tomorrow")
async def get_tomorrow(message: types.Message) -> None:
    dt_tomorrow = date.today() + timedelta(days=1)
    tomorrow = dt_tomorrow.strftime(DATE_FORMAT)

    events = get_events()

    if tomorrow in events:
        event = f"{hbold(events[tomorrow]['date'])}\n\
            {events[tomorrow]['event']}"

        await message.reply(event)

    else:
        await message.reply("Nothing for tomorrow.")


@dp.message_handler()
async def get_day(message: types.Message) -> None:
    # Getting user date for searching event
    tmpl_date = "$year-$input_date"
    input_date = Template(tmpl_date).substitute(
        year=datetime.today().year, input_date=message.text
    )
    dt_input = datetime.strptime(input_date, DATE_FORMAT)
    target_date = dt_input.date().strftime(DATE_FORMAT)

    events = get_events()

    if target_date in events:
        event = f"{hbold(events[target_date]['date'])}\n\
            {events[target_date]['event']}"

        await message.reply(event)

    else:
        await message.reply(f"Nothing for {message.text}.")


# async def check_events_every_day() -> None:
#     while True:
#         new_events: dict = check_new_events()
#         # chat_id = message.chat.id
#
#         if new_events:
#             for key, value in new_events.items():
#                 event: str = f"{hbold(value['date'])}\n{value['event']}"
#
#                 await bot.send_message(chat_id, event, disable_notification=True)
#
#         else:
#             await bot.send_message(chat_id, "Nothing new...", disable_notification=True)
#
#         await asyncio.sleep(5)


if __name__ == "__main__":
    #  loop = asyncio.get_event_loop()
    #  loop.create_task(check_events_every_day())
    executor.start_polling(dp)
