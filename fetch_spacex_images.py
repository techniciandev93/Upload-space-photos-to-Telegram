import argparse
from pathlib import Path
import requests
from services import get_extension, download_image


def fetch_spacex_last_launch(path, launch_id):
    spacex_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    Path(path).mkdir(parents=True, exist_ok=True)
    response = requests.get(spacex_url)
    response.raise_for_status()
    images = response.json()['links']['flickr']['original']
    for number, image_url in enumerate(images):
        response = requests.get(image_url)
        response.raise_for_status()
        extension = get_extension(image_url)
        download_image(image_url, path, f'spacex_{number}{extension}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Сохраняет изображения с последнего запуска SpaceX. Просто укажите "
                                                 "ID запуска или ничего не указывайте и тогда получите изображения с "
                                                 "последнего запуска. python fetch_spacex_images.py или python "
                                                 "fetch_spacex_images.py [id]")
    parser.add_argument("id", help="id запуска ракеты", nargs='?', default='latest')
    args = parser.parse_args()

    fetch_spacex_last_launch('images/', args.id)
