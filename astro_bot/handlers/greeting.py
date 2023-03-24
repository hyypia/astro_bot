from aiogram import Dispatcher, types

from templates import GREETING_MESSAGE
from services.events import db_init
from keyboards.reply_keyboard import location_keyboard


async def greeting(message: types.Message):
    await db_init()
    await message.answer(GREETING_MESSAGE, reply_markup=location_keyboard())


def register_handler_start(dp: Dispatcher):
    dp.register_message_handler(greeting, commands=["Start", "start"])
