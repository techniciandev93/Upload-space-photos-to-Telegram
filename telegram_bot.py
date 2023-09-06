import os
import telegram
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    telegram_api_token = os.environ['TELEGRAM_API_TOKEN']
    telegra_group_chat_id = os.environ['TELEGRAM_GROUP_CHAT_ID']
    bot = telegram.Bot(token=telegram_api_token)
    bot.send_message(chat_id=telegra_group_chat_id, text="Hello world")
