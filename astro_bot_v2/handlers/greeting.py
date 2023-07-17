from aiogram import Dispatcher, types

from templates import GREETING_MESSAGE
from keyboards.reply_keyboard import location_kayboard


async def greeting(message: types.Message) -> None:
    await message.answer(GREETING_MESSAGE, reply_markup=location_kayboard())


def register_handler_start(dp: Dispatcher) -> None:
    dp.register_message_handler(greeting, commands=["Start", "start"])
