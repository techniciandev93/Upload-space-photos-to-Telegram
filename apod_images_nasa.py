import argparse
import os
from pathlib import Path
import requests
from dotenv import load_dotenv
from services import get_extension, save_file


def download_apod_images(api_token, path, image_count):
    params = {'api_key': api_token, 'thumbs': 'false', 'count': image_count}
    nasa_url = f'https://api.nasa.gov/planetary/apod'
    Path(path).mkdir(parents=True, exist_ok=True)
    response = requests.get(nasa_url, params=params)
    response.raise_for_status()
    for number, image_url in enumerate(response.json()):
        response = requests.get(image_url['url'])
        response.raise_for_status()
        extension = get_extension(image_url['url'])
        save_file(response.content, path, f'nasa_apod_{number}{extension}')


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']

    parser = argparse.ArgumentParser(description="Для загрузки фотографий изображения дня (APOD) от NASA. Укажите "
                                     "количество изображений, и скрипт загрузит их. python apod_images_nasa.py [count]")
    parser.add_argument("count", help="Укажите количество фотографий", nargs='?', default='30')
    args = parser.parse_args()

    download_apod_images(nasa_api_key, 'images/', args.count)
