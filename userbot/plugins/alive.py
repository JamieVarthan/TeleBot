# For @TeleBotHelp
"""Check if your userbot is working."""
import asyncio
import requests
from PIL import Image
from io import BytesIO
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet, check pinned in @TeleBotHelp"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    
    req = requests.get("https://telegra.ph/file/f58aa88c51c6f7473eb12.jpg")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_message(alive.chat_id, f"**Welcome To Spade User Bot **\n\n"
            "**`Hey! I'm Spade Security System !!.`**\n\n"
            "` 🔸 Userbot version:` **1.0**\n` 🔹 Python:` **3.5**\n"
            "` 🔸 More info:` No More INFO , Write your Own Python Code!!\n"
            "` 🔹 Bot created by:` [Spade](https://t.me/wolverine_smash)\n"
            "` 🔸 Database Status:` **My name is Athena!**\n"
            f"` 🔹 My Rightful owner`:  [Athena](https://t.me/athena_the_warrior)\n\n"
            "    [✨ Private Bot Service , If needed contact My Owner ✨](https://t.me/wolverine_smash)", link_preview = False)
        await borg.send_file(alive.chat_id, file=sticker) 
        await alive.delete()
