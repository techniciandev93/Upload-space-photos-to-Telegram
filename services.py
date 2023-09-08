import os
from urllib.parse import urlparse


def save_file(file_bytes, path, file_name):
    with open(f'{path}{file_name}', 'wb') as file:
        file.write(file_bytes)


def get_file(path):
    with open(path, 'rb') as file:
        return file


def get_extension(url):
    path = urlparse(url).path
    extension = os.path.splitext(path)[-1]
    return extension
