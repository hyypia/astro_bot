from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from templates import START_MESSAGE
from keyboards.reply_keyboard import main_keyboard


async def start(message: types.Message):
    user_data = {
        "id": message.from_user.id,
        "name": message.from_user.full_name,
        "username": message.from_user.username,
        "timezone": "GMT",
    }
    text = message.text
    if text == "GMT":
        print(user_data)
        await message.answer(text, reply_markup=main_keyboard())
    else:
        user_data["timezone"] = message.location
        print(user_data)
        await message.answer(START_MESSAGE, reply_markup=main_keyboard())


def register_handler_start(dp: Dispatcher):
    dp.register_message_handler(start, content_types=["location"])
    dp.register_message_handler(start, Text(equals="GMT"))
