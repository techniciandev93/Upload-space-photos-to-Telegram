import os
from datetime import datetime
from dotenv import load_dotenv
from services import send_request, save_file


def download_images_planet_earth(api_key, path):
    nasa_url = f'https://api.nasa.gov/EPIC/api/natural?api_key={api_key}'
    response_json = send_request(nasa_url).json()
    for data_camera in response_json:
        image = f"{data_camera['image']}.png"
        date = datetime.strptime(data_camera['date'], '%Y-%m-%d %H:%M:%S')
        format_date = date.strftime("%Y/%m/%d")
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{format_date}/png/{image}?api_key={api_key}'
        image_bytes = send_request(image_url).content
        save_file(image_bytes, path, image)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']

    download_images_planet_earth(nasa_api_key, 'images/')
