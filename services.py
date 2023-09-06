import os
import requests
from urllib.parse import urlparse


def send_request(url):
    response = requests.get(url)
    response.raise_for_status()
    return response


def save_file(file_bytes, path, file_name):
    with open(f'{path}{file_name}', 'wb') as file:
        file.write(file_bytes)


def get_extension(url):
    path = urlparse(url).path
    extension = os.path.splitext(path)[-1]
    return extension
