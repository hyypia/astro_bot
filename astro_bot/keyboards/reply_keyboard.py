from aiogram.types import ReplyKeyboardMarkup

buttons = ['help', 'week', "new", "yesterday", "today", "tomorrow", "image"]
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(*buttons)
