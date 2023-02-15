from aiogram import Dispatcher, types

from templates import HELP


async def help_(message: types.Message) -> None:
    await message.reply(HELP)


def register_handler_help(dp: Dispatcher) -> None:
    dp.register_message_handler(help_, commands="help")
