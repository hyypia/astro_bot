import asyncio
import logging
from aiogram import Bot, Dispatcher, types

from config import TOKEN, LOGGING_FORMAT
from handlers import start, help_, events, image


async def main():
    logging.basicConfig(
        filename="astro_bot.log",
        filemode="w",
        format=LOGGING_FORMAT,
        level=logging.DEBUG,
    )
    logging.info("Start application")

    bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot)

    start.register_handler_start(dp)
    help_.register_handler_help(dp)
    image.register_handler_image(dp)
    events.register_handler_events(dp)

    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
