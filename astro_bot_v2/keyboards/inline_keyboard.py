from aiogram import types


def get_inline_week_keyboard() -> types.InlineKeyboardMarkup:
    next_prev_buttons = [
        types.InlineKeyboardButton(text="<", callback_data="week_previous"),
        types.InlineKeyboardButton(text=">", callback_data="week_next"),
    ]
    next_prev_keyboard = types.InlineKeyboardMarkup()
    next_prev_keyboard.add(*next_prev_buttons)

    return next_prev_keyboard


def get_inline_new_button() -> types.InlineKeyboardMarkup:
    next_button = types.InlineKeyboardButton(text="next", callback_data="next")
    next_key = types.InlineKeyboardMarkup()
    next_key.add(next_button)

    return next_key
