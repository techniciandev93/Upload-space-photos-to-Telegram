import argparse
import os
from pathlib import Path
from dotenv import load_dotenv
from services import send_request, get_extension, save_file


def download_apod_images(api_token, path, image_count):
    nasa_url = f'https://api.nasa.gov/planetary/apod?thumbs=false&count={image_count}&api_key={api_token}'
    Path(path).mkdir(parents=True, exist_ok=True)
    response_json = send_request(nasa_url).json()
    for number, image_url in enumerate(response_json):
        response_image_byte = send_request(image_url['url']).content
        extension = get_extension(image_url['url'])
        save_file(response_image_byte, path, f'nasa_apod_{number}{extension}')


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']

    parser = argparse.ArgumentParser()
    parser.add_argument("count", help="Укажите количество фотографий", nargs='?', default='30')
    args = parser.parse_args()

    download_apod_images(nasa_api_key, 'images/', args.count)
