create_users_table = """CREATE TABLE IF NOT EXISTS users (
    telegram_id BIGINT PRIMARY KEY,
    user_name TEXT NOT NULL,
    name TEXT,
    timezone TEXT NOT NULL
    )"""

create_events_table = """CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    iso_date TEXT NOT NULL,
    date TEXT NOT NULL,
    week_num INTEGER,
    description TEXT NOT NULL
    )"""

create_user_ins = """INSERT INTO
    users (telegram_id, user_name, name, timezone)
    VALUES (?, ?, ?, ?)"""

create_event_ins = """INSERS INTO
    events (id, iso_date, date, week_num, description)
    VALUES (?, ?, ?, ?, ?)"""

select_users_id = "SELECT telegram_id from users"
