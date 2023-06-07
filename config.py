from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = '27153901'
APP_HASH = 'b3ab002ac2101538a80ce0e2064f6894'
BOT_USERNAME = 'Hsud8snsidehbot'
session = os.environ.get("TERMUX")
SESSION = os.environ.get("TERMUX")
token = '6269170972:AAHg3CxD12uPHAr926U611WX126Kha5cj2E'
sython = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()

