import requests
import os
import time


def get_apod_data():
    """This function gets the APOD data for today from NASA and returns it.
    :return: response: dict
    """
    API_KEY = os.getenv("NASA_API_KEY")
    date = time.strftime("%Y-%m-%d")
    url = f"https://api.nasa.gov/planetary/apod?" \
          f"date={date}&" \
          f"api_key={API_KEY}"
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    print(get_apod_data())