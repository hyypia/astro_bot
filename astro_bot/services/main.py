import json
from .spider import get_url, save_content
from .parse_data import cut_content, make_events_dict
from config import FILE_NAME, DB


def get_content():
    link = get_url()
    content = save_content(link)
    with open(FILE_NAME, "wt") as file:
        file.writelines(content)
        f_name = file.name

    lst = cut_content(f_name)
    events = make_events_dict(lst)
    with open(DB, "w") as db:
        json.dump(events, db, ensure_ascii=False, indent="\t")


def check_new_events():
    with open(DB, "r") as db:
        events_dict = json.load(db)

    new_events = {}
    link = get_url()
    content = save_content(link)

    with open(FILE_NAME, "wt") as file:
        file.writelines(content)
        f_name = file.name

    lst = cut_content(f_name)
    events = make_events_dict(lst)

    if events:
        for date in events:
            if date in events_dict:
                continue
            else:
                events_dict[date] = events[date]
                new_events[date] = events[date]

    with open(DB, "w") as file:
        json.dump(events_dict, file, ensure_ascii=False, indent="\t")

    return new_events


def get_events():
    with open(DB, "r") as db:
        events = json.load(db)

    return events


def main():
    get_content()
    print(check_new_events())


if __name__ == "__main__":
    main()
