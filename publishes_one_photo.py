import argparse
import os
import random
import telegram
from dotenv import load_dotenv
from services import get_file
from telegram_bot import get_image_paths


def publishes_photo(tg_bot, chat_id, image_path, image):
    if not image:
        image = random.choice(get_image_paths(image_path))
    image = os.path.join(image_path, image)
    tg_bot.send_photo(chat_id, photo=get_file(image))


if __name__ == '__main__':
    load_dotenv()
    telegram_api_token = os.environ['TELEGRAM_API_TOKEN']
    telegram_group_chat_id = os.environ['TELEGRAM_GROUP_CHAT_ID']

    parser = argparse.ArgumentParser(description="Для публикации одной фотографии в чате. Отправьте выбранное "
                                                 "изображение или дайте скрипту выбрать случайное изображение из "
                                                 "заданной директории. python publishes_one_photo.py или python "
                                                 "publishes_one_photo.py nasa_apod_29.gif")
    parser.add_argument("image", help="Введите наименование фотографии", nargs='?', default=None)
    args = parser.parse_args()

    bot = telegram.Bot(token=telegram_api_token)
    image_path = 'images/'
    publishes_photo(bot, telegram_group_chat_id, image_path, args.image)
