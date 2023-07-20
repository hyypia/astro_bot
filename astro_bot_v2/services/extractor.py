import astro_bot_v2.services.scrap_data as sd
import astro_bot_v2.services.parse_data as pd


def extract_data() -> dict:
    data = sd.get_data()
    data_dict = pd.parse_scraped_data_to_dict(data)
    return data_dict
