import logging
import asyncio
from aiogram import Bot, Dispatcher, types

from config import TOKEN, LOGGING_FORMAT, LOGGING_FILE, LOGGING_MODE
from handlers import greeting, start, help_, week, today, yesterday, tomorrow


logging.basicConfig(
    format=LOGGING_FORMAT,
    filename=LOGGING_FILE,
    filemode=LOGGING_MODE,
    level=logging.INFO,
)


async def main() -> None:
    logging.info("Start application")
    bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot)

    greeting.register_handler_start(dp)
    start.register_handler_start(dp)
    help_.register_handler_help(dp)
    week.register_handler_week(dp)
    today.register_handler_today(dp)
    yesterday.register_handler_yesterday(dp)
    tomorrow.register_handler_tomorrow(dp)

    await dp.start_polling()


if __name__ == "__main__":
    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        print("\nApplication closed")
        logging.info("Application closed")

    except Exception as err:
        logging.error(err)
