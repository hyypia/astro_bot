from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from services.events import get_events
from templates import MESSAGE_WITH_EVENT
from keyboards.inline_keyboard import get_inline_week_keyboard


user_days_counter = {}


async def make_msg_with_one_day(days_count: int) -> str:
    events = await get_events()
    events_list = list(events.items())
    _, event = events_list[-(days_count)]
    msg = MESSAGE_WITH_EVENT(event)

    return msg


async def get_week_msg_text(message: types.Message) -> None:
    msg = await make_msg_with_one_day(7)
    await message.answer(msg, reply_markup=get_inline_week_keyboard())


async def update_week_msg_text(message: types.Message, day_num: int):
    msg = await make_msg_with_one_day(day_num)
    await message.edit_text(msg, reply_markup=get_inline_week_keyboard())


async def callbacks_counter(call: types.CallbackQuery) -> None:

    days_counter = user_days_counter.get(call.from_user.id, 7)
    action = call.data.split("_")[1]

    if action == "previous":
        user_days_counter[call.from_user.id] = days_counter + 1

        await update_week_msg_text(call.message, days_counter + 1)

    elif action == "next":
        user_days_counter[call.from_user.id] = days_counter - 1

        await update_week_msg_text(call.message, days_counter - 1)

    await call.answer()


def register_handler_week(dp: Dispatcher):
    dp.register_message_handler(get_week_msg_text, Text(equals="Week"))
    dp.register_callback_query_handler(callbacks_counter, Text(startswith="week_"))