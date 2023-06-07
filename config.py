from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = '26272949'
APP_HASH = '0e740796455d992a273fc1df79effcd1'
BOT_USERNAME = os.environ.get("BOT_USERNAME")
session = os.environ.get("TERMUX")
SESSION = os.environ.get("TERMUX")
token = os.environ.get("TOKEN")
sython = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()

