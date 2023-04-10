from string import Template
from datetime import datetime

from aiogram import Dispatcher, types

from config import DATE_FORMAT
from handlers.events import get_message_for_user


async def get_day(message: types.Message):
    # Getting event for certain date from db

    tmpl_date = "$year-$input_date"
    input_date = Template(tmpl_date).substitute(
        year=datetime.today().year, input_date=message.text
    )
    dt_input = datetime.strptime(input_date, DATE_FORMAT)
    target_date = dt_input.date().strftime(DATE_FORMAT)

    msg = await get_message_for_user(target_date)

    await message.reply(msg)


def register_handler_certain_day(dp: Dispatcher):
    dp.register_message_handler(get_day)
