from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from services.image import get_image
from templates import MESSAGE_WITH_IMAGE


async def get_image_of_the_day(message: types.Message):
    res = get_image()
    if res:
        img, msg = MESSAGE_WITH_IMAGE(res.json())

        await message.reply_photo(img, msg)


def register_handler_image(dp: Dispatcher):
    dp.register_message_handler(get_image_of_the_day, Text(equals="image"))
