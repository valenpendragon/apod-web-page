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


def get_image_data(url, filepath="images/today.jpg"):
    """This function downloads the image file from the supplied URL,
    overwriting previous files. It returns a bool indicating success or
    failure to retrieve the image: True if successful, False otherwise.
    :param url: str
    :return: bool
    """
    try:
        response = requests.get(url)
    except ConnectionError:
        return False
    else:
        try:
            with open(filepath, "wb") as file:
                file.write(response.content)
        except IOError:
            return False
        else:
            return True

if __name__ == "__main__":
    apod_data = get_apod_data()
    print(apod_data)
    img_get = get_image_data(apod_data["url"])
    print(img_get)