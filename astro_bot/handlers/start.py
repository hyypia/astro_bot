from aiogram import Dispatcher, types

from templates import GREETING
from services.events import db_init
from keyboards.reply_keyboard import keyboard


async def start(message: types.Message):
    await db_init()
    await message.answer(GREETING, reply_markup=keyboard)


def register_handler_start(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start"])
