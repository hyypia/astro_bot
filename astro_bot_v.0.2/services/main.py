import scrap_data as sd
import parse_data as pd


def main():
    data = sd.get_data()
    data_dict = pd.parse_scraped_data_to_dict(data)
    print(len(data_dict))


if __name__ == "__main__":
    main()
