import time
import psutil

from datetime import datetime

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from TOGA import app, StartTime, BOT_NAME, BOT_USERNAME
from TOGA.Helpers import get_readable_time


@app.on_message(filters.command("ping"))
async def ping_fallen(_, message: Message):
    hmm = await message.reply_photo(
        photo=config.PING_IMG,
        caption=f"{BOT_NAME} ɪs ᴘɪɴɢɪɴɢ..."
    )
    upt = int(time.time() - StartTime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    start = datetime.now()
    resp = (datetime.now() - start).microseconds / 1000
    uptime = get_readable_time((upt))

    await hmm.edit_text(
        f""" ᴩᴏɴɢ : `{resp}ᴍs`
<b><u>{BOT_NAME} System Stats :</u></b>
**ᴜᴩᴛɪᴍᴇ :** {uptime}
**ʀᴀᴍ :** {mem}
**ᴄᴩᴜ :** {cpu}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ㅤ", url=f"https://t.me/toga_robot?startgroup=new"
                    )
                ],
            ]
        ),
    )
