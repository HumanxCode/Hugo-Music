import requests
from pyrogram import Client as Bot

from HugoMusic.config import API_HASH
from HugoMusic.config import API_ID
from HugoMusic.config import BG_IMAGE
from HugoMusic.config import BOT_TOKEN
from HugoMusic.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="HugoMusic.modules"),
)

bot.start()
run()
