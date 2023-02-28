from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from templates import HELP


async def help_(message: types.Message):
    await message.reply(HELP)


def register_handler_help(dp: Dispatcher):
    dp.register_message_handler(help_, Text(equals="help"))
