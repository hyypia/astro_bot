from services.req import make_req


def get_image():
    res = make_req(
        "https://api.nasa.gov/planetary/apod?api_key=fXQ5MaFBHMZP7oiG4usDKm9ZgcR1Brl06LmAOyts"
    )
    return res
