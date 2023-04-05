from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from timezonefinder import TimezoneFinder

from templates import START_MESSAGE
from services.events import add_user
from keyboards.reply_keyboard import main_keyboard


async def start(message: types.Message):
    user_data = {
        "telegram_id": message.from_user.id,
        "name": message.from_user.full_name,
        "username": message.from_user.username,
        "timezone": "GMT",
    }

    if message.text != "GMT":
        tf = TimezoneFinder()
        user_data["timezone"] = tf.timezone_at(
            lng=message.location.longitude, lat=message.location.latitude
        )

    await add_user(user_data)
    await message.answer(START_MESSAGE, reply_markup=main_keyboard())


def register_handler_start(dp: Dispatcher):
    dp.register_message_handler(start, content_types=["location"])
    dp.register_message_handler(start, Text(equals="GMT"))
