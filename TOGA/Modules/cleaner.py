import os

from pyrogram import filters
from pyrogram.types import Message

from TOGA import app, OWNER


@app.on_message(filters.command(["clearcache", "rmdownloads"]) & filters.user(OWNER))
async def clear_misc(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    downloads = os.path.realpath("downloads")
    raw_files = os.path.realpath("raw_files")
    down_dir = os.listdir(downloads)
    raw_dir = os.listdir(raw_files)
    pth = os.path.realpath(".")
    os_dir = os.listdir(pth)

    if down_dir:
        for file in down_dir:
            os.remove(os.path.join(downloads, file))
    if raw_dir:
        for file in raw_dir:
            os.remove(os.path.join(raw_files, file))
    if os_dir:
        for lel in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
    await message.reply_text("» ᴀʟʟ ᴛᴇᴍᴘ ᴅɪʀᴇᴄᴛᴏʀɪᴇs ᴄʟᴇᴀɴᴇᴅ.")
