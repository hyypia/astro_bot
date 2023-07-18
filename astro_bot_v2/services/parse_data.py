import re


def parse_scraped_data_to_dict(source_data: str) -> dict:
    """Parsing row data from string format to dictionary and return it"""

    # Find dates and cut data for every date
    date_pattern = re.compile(r"^\w+,\s\w+\s\d+", re.MULTILINE)
    dates = date_pattern.findall(source_data)
    other_content = date_pattern.split(source_data)

    # Cutting from description of event redundant and append neccessary
    # data to list
    events = []
    for event in other_content:
        if event:
            event = event[: event.find("Sunrise")]
            events.append(event)

    # Build dictionary
    data_dict = dict(zip(dates, events))
    return data_dict
