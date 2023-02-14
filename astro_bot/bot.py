import asyncio
import logging
from aiogram import Bot, Dispatcher, types

from config import TOKEN
from handlers import start, events


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot)

    start.register_handler_start(dp)
    events.register_handler_week(dp)

    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
