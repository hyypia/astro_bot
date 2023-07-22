create_users_table = """CREATE TABLE IF NOT EXISTS users (
    telegram_id BIGINT PRIMARY KEY,
    user_name TEXT NOT NULL,
    name TEXT,
    timezone TEXT
    )"""

create_events_table = """CREATE TABLE IF NOT EXISTS events (
    row_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL
    )"""

create_user_ins = """INSERT INTO
    users (telegram_id, user_name, name, timezone)
    VALUES (?, ?, ?, ?)"""

create_event_ins = """INSERT INTO
    events (date, description)
    VALUES (?, ?)"""

select_users_id = "SELECT telegram_id FROM users"

select_events = "SELECT date, description FROM events"

select_events_ids = "SELECT date_id FROM events"


def select_last_new_events(count: int):
    return f"SELECT date, description FROM events ORDER BY row_id DESC LIMIT {count}"


def select_certain_event(date: str) -> str:
    return f"SELECT date, description FROM events WHERE date='{date}'"
