from aiogram import Dispatcher, types
from templates import GREETING


async def start(message: types.Message) -> None:
    await message.answer(GREETING)


def register_handler_start(dp: Dispatcher):
    dp.register_message_handler(start, commands=["start", "help"])
