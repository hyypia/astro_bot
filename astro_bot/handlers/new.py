from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text

from services.events import check_new_events, get_events
from keyboards.inline_keyboard import get_inline_new_button
from templates import MESSAGE_WITH_EVENT, NOTHING_NEWS_FOUND


user_days_counter = {}
new_events = {}


def make_msg_with_one_event(events: dict, day_num=0) -> str:
        date, event = list(events.items())[-(day_num or len(events))]
        return MESSAGE_WITH_EVENT(event)


async def get_new_days(message: types.Message):
    new_events = await check_new_events()
    user_days_counter[message.from_user.id] = len(new_events)

    if new_events and len(new_events) > 1:
        msg = make_msg_with_one_event(new_events)
        # _, event = list(new_events.items())[-(len(new_events))]
        # msg = MESSAGE_WITH_EVENT(event)

        await message.answer(msg, reply_markup=get_inline_new_button())

    elif new_events and len(new_events) == 1:
        msg = make_msg_with_one_event(new_events)
        # _, event = list(new_events.items())[-(len(new_events))]
        # msg = MESSAGE_WITH_EVENT(event)

        await message.answer(msg)

    else:
        await message.answer(NOTHING_NEWS_FOUND)


async def update_new_days_msg_text(message: types.Message, events: dict, day_num: int):
    events = await get_events()

    if day_num > 1:
        msg = make_msg_with_one_event(events, day_num)
        # _, event = list(events.items())[-(day_num)]
        # msg = MESSAGE_WITH_EVENT(event)

        await message.edit_text(msg, reply_markup=get_inline_new_button())

    elif day_num == 1:
        msg = make_msg_with_one_event(events, day_num)
        # _, event = list(events.items())[-(day_num)]
        # msg = MESSAGE_WITH_EVENT(event)

        await message.edit_text(msg)


async def callback_counter(call: types.CallbackQuery):
    days_counter = user_days_counter.get(call.from_user.id, 0)

    if call.data == "next":
        user_days_counter[call.from_user.id] = days_counter - 1

        await update_new_days_msg_text(call.message, new_events, days_counter - 1)

    await call.answer()


def register_handler_new_days(dp: Dispatcher):
    dp.register_message_handler(get_new_days, Text(equals="New"))
    dp.register_callback_query_handler(callback_counter, Text(equals="Next"))
