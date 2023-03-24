from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        "Help",
        "Week",
        "New",
        "Yesterday",
        "Today",
        "Tomorrow",
        "Image of the day",
    ]
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)

    return keyboard


def location_keyboard() -> ReplyKeyboardMarkup:
    location_key = KeyboardButton("Share location", request_location=True)
    gmt_key = KeyboardButton("GMT")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(location_key, gmt_key)

    return keyboard
