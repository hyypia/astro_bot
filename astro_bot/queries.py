create_users_table = """CREATE TABLE IF NOT EXISTS users (
    telegram_id BIGINT PRIMARY KEY,
    user_name TEXT NOT NULL,
    name TEXT,
    timezone TEXT NOT NULL
    )"""

create_events_table = """CREATE TABLE IF NOT EXISTS events (
    iso_date TEXT NOT NULL PRIMARY KEY,
    date TEXT NOT NULL,
    week_num INTEGER,
    description TEXT NOT NULL
    )"""

create_user_ins = """INSERT INTO
    users (telegram_id, user_name, name, timezone)
    VALUES (?, ?, ?, ?)"""

create_event_ins = """INSERT INTO
    events (iso_date, week_num, date, description)
    VALUES (?, ?, ?, ?)"""

select_users_id = "SELECT telegram_id FROM users"

select_events = "SELECT date, description FROM events"


def select_certain_event(date: str) -> str:
    return f"SELECT date, description FROM events WHERE iso_date='{date}'"
