import os
from datetime import datetime
import requests
from dotenv import load_dotenv
from services import download_image


def download_images_planet_earth(api_key, path):
    params = {'api_key': api_key}
    nasa_url = f'https://api.nasa.gov/EPIC/api/natural'
    response = requests.get(nasa_url, params=params)
    response.raise_for_status()
    for space_images in response.json():
        image = f"{space_images['image']}.png"
        date = datetime.strptime(space_images['date'], '%Y-%m-%d %H:%M:%S')
        format_date = date.strftime("%Y/%m/%d")
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{format_date}/png/{image}'
        download_image(image_url, path, image)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']

    download_images_planet_earth(nasa_api_key, 'images/')
