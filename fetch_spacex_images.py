import argparse
from pathlib import Path
from services import send_request, get_extension, save_file


def fetch_spacex_last_launch(path, launch_id):
    spacex_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    Path(path).mkdir(parents=True, exist_ok=True)
    response = send_request(spacex_url).json()
    images = response['links']['flickr']['original']
    for number, image_url in enumerate(images):
        response_image_byte = send_request(image_url).content
        extension = get_extension(image_url)
        save_file(response_image_byte, path, f'spacex_{number}{extension}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("id", help="id запуска ракеты", nargs='?', default='latest')
    args = parser.parse_args()

    fetch_spacex_last_launch('images/', args.id)
