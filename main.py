import os
import requests
from pathlib import Path
from urllib.parse import urlparse
from dotenv.main import load_dotenv
from datetime import datetime


def send_request(url):
    response = requests.get(url)
    response.raise_for_status()
    return response


def save_file(file_bytes, path, file_name):
    with open(f'{path}{file_name}', 'wb') as file:
        file.write(file_bytes)


def fetch_spacex_last_launch(path):
    spacex_url = "https://api.spacexdata.com/v5/launches/5eb87ce4ffd86e000604b337"
    Path(path).mkdir(parents=True, exist_ok=True)
    response = send_request(spacex_url).json()
    images = response['links']['flickr']['original']
    for number, image_url in enumerate(images):
        response_image_byte = send_request(image_url).content
        extension = get_extension(image_url)
        save_file(response_image_byte, path, f'spacex_{number}{extension}')


def download_apod_images(api_token, path):
    nasa_url = f'https://api.nasa.gov/planetary/apod?count=30&api_key={api_token}'
    Path(path).mkdir(parents=True, exist_ok=True)
    response_json = send_request(nasa_url).json()
    for number, image_url in enumerate(response_json):
        response_image_byte = send_request(image_url['url']).content
        extension = get_extension(image_url['url'])
        save_file(response_image_byte, path, f'nasa_apod_{number}{extension}')


def planet_earth(api_key, path):
    nasa_url = f'https://api.nasa.gov/EPIC/api/natural?api_key={api_key}'
    response_json = send_request(nasa_url).json()
    for data_camera in response_json[:10]:
        image = f"{data_camera['image']}.png"
        date = datetime.strptime(data_camera['date'], '%Y-%m-%d %H:%M:%S')
        format_date = date.strftime("%Y/%m/%d")
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{format_date}/png/{image}?api_key={api_key}'
        image_bytes = send_request(image_url).content
        save_file(image_bytes, path, image)


def get_extension(url):
    path = urlparse(url).path
    extension = os.path.splitext(path)[-1]
    return extension


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']

    fetch_spacex_last_launch('images/')
    download_apod_images(nasa_api_key, 'images/')
    planet_earth(nasa_api_key, 'images/')
