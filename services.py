import os
from urllib.parse import urlparse
import requests


def get_file(path):
    with open(path, 'rb') as file:
        return file


def get_extension(url):
    path = urlparse(url).path
    extension = os.path.splitext(path)[-1]
    return extension


def download_image(image_url, path, file_name):
    response = requests.get(image_url)
    response.raise_for_status()
    with open(f'{path}{file_name}', 'wb') as file:
        file.write(response.content)
