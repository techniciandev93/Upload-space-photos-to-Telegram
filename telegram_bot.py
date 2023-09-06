import os
import telegram
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    telegram_api_token = os.environ['TELEGRAM_API_TOKEN']
    telegra_group_chat_id = os.environ['TELEGRAM_GROUP_CHAT_ID']
    nasa_api_key = os.environ['NASA_API_KEY']
    bot = telegram.Bot(token=telegram_api_token)

    image_url = 'https://api.nasa.gov/EPIC/archive/natural/2019/05/30/png/epic_1b_20190530011359.png?api_key' \
                f'={nasa_api_key}'
    bot.send_photo(telegra_group_chat_id, photo=image_url)
