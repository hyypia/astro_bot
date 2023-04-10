import asyncio
import logging
from aiogram import Bot, Dispatcher, types

from config import TOKEN, LOGGING_FORMAT
from handlers import greeting, start, help_, week, events, image, certain_day


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

    greeting.register_handler_start(dp)
    start.register_handler_start(dp)
    help_.register_handler_help(dp)
    image.register_handler_image(dp)
    week.register_handler_week(dp)
    events.register_handler_events(dp)
    certain_day.register_handler_certain_day(dp)

    await dp.start_polling()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nApplication closed")
    except Exception:
        logging.error(Exception)
