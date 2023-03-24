from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from services.image import get_image
from templates import MESSAGE_WITH_IMAGE, NOTHING_NEWS_FOUND


async def get_image_of_the_day(message: types.Message):
    resp = get_image()
    if resp:
        img, msg = MESSAGE_WITH_IMAGE(resp.json())

        await message.reply_photo(img, msg)
    else:
        await message.answer(NOTHING_NEWS_FOUND)


def register_handler_image(dp: Dispatcher):
    dp.register_message_handler(get_image_of_the_day, Text(startswith="Image"))
