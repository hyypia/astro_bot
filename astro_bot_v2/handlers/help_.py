from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from astro_bot_v2.templates import HELP_MESSAGE


async def help_(message: types.Message) -> None:
    await message.reply(HELP_MESSAGE)


def register_handler_help(dp: Dispatcher) -> None:
    dp.register_message_handler(help_, Text(equals="Help"))
