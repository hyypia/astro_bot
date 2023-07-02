import re


def parse_scraped_data_to_dict(source_data: str) -> dict:
    date_pattern = re.compile(r"^\w+,\s\w+\s\d+", re.MULTILINE)
    dates = date_pattern.findall(source_data)
    other_content = date_pattern.split(source_data)
    events = []
    for event in other_content:
        if event:
            event = event[: event.find("Sunrise")]
            events.append(event)
    data_dict = dict(zip(dates, events))
    return data_dict
