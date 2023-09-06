import argparse
import os
import random
import time
import telegram
from dotenv import load_dotenv


def get_image_paths(path):
    file_paths = []
    for root, dirs, files in os.walk(path):
        for file_name in files:
            file_paths.append(os.path.join(root, file_name))
    return file_paths


def get_one_image(images):
    for image in images:
        yield image


def sender_image_main(tg_bot, path, chat_id, delay):
    image_paths = get_image_paths(path)
    gen_images = get_one_image(image_paths)
    while True:
        try:
            image = next(gen_images)
            tg_bot.send_photo(chat_id, photo=open(image, 'rb'))
            time.sleep(delay * 60 * 60)
        except StopIteration:
            random.shuffle(image_paths)
            gen_images = get_one_image(image_paths)
        except telegram.error.NetworkError:
            continue


if __name__ == '__main__':
    load_dotenv()
    telegram_api_token = os.environ['TELEGRAM_API_TOKEN']
    telegram_group_chat_id = os.environ['TELEGRAM_GROUP_CHAT_ID']

    parser = argparse.ArgumentParser()
    parser.add_argument("delay", help="Введите время задержки в часах", nargs='?', default=4)
    args = parser.parse_args()

    bot = telegram.Bot(token=telegram_api_token)
    image_path = 'images/'
    sender_image_main(bot, image_path, telegram_group_chat_id, args.delay)
