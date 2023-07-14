from . import scrap_data as sd
from . import parse_data as pd


def extract_data():
    data = sd.get_data()
    data_dict = pd.parse_scraped_data_to_dict(data)
    return data_dict


def main():
    extract_data()


if __name__ == "__main__":
    main()
