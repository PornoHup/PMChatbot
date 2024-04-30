#-------------------------------------- https://github.com/m4mallu/PMChatbot ------------------------------------------#
import os
import logging

from pyrogram import Client

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config

if __name__ == "__main__":
    plugins = dict(root="plugins")
    bot = Client(EsillaRobot
        "pmbot",
        bot_token=Config.6838039674:AAFepR2b-U1Sjjztwx4AUQhwAuEQs2GKRqk,
        api_id=Config.12349641,
        api_hash=Config.0f9159afc920f9c592df555e4b1cb73b,
        plugins=plugins
    )
    bot.run()
