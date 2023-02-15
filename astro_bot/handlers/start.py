from aiogram import Dispatcher, types

from templates import GREETING
from services.events import db_init


async def start(message: types.Message) -> None:
    await db_init()
    await message.answer(GREETING)


def register_handler_start(dp: Dispatcher) -> None:
    dp.register_message_handler(start, commands=["start"])
