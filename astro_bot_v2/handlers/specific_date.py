from string import Template
from datetime import datetime

from aiogram import Dispatcher, types

from astro_bot_v2.handlers.get_specific_date_event import get_message_for_user


async def get_day(message: types.Message) -> None:
    date_template = "$weekday, $input_date"
    year = datetime.today().year
    target_date = Template(date_template).substitute(
        weekday=datetime.strptime(f"{year} {message.text}", "%Y %B %d").strftime("%A"),
        input_date=message.text,
    )

    msg = get_message_for_user(target_date)

    await message.reply(msg)


def register_handler_specific_day(dp: Dispatcher) -> None:
    dp.register_message_handler(get_day)
