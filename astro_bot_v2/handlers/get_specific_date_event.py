from services.events import get_events
from templates import MESSAGE_WITH_EVENT, NOTHING_NEWS_FOUND


def get_message_for_user(date: str) -> str:
    event = get_events(date=date)
    if event:
        day, description = event[0]
        return MESSAGE_WITH_EVENT(day, description)
    else:
        return NOTHING_NEWS_FOUND
