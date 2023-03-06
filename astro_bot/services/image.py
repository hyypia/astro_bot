from services.req import make_req
from config import IMAGE_OF_THE_DAY_URL


def get_image():
    res = make_req(IMAGE_OF_THE_DAY_URL)

    return res
