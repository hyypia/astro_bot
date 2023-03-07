from aiogram import types


def get_inline_keyboard() -> types.InlineKeyboardMarkup:
    next_prev_buttons = [
        types.InlineKeyboardButton(text="<", callback_data="event_previous"),
        types.InlineKeyboardButton(text=">", callback_data="event_next"),
    ]
    next_prev_keyboard = types.InlineKeyboardMarkup()
    next_prev_keyboard.add(*next_prev_buttons)

    return next_prev_keyboard
