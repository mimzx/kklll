import time

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message, InlineKeyboardMarkup

import config

from FallenMusic import (
    app,
    BOT_NAME,
    BOT_USERNAME,
    OWNER,
    StartTime,
)
from FallenMusic.Helpers import (get_readable_time,
                                 pm_buttons, gp_buttons)
from FallenMusic.Helpers.dossier import *


@app.on_message(filters.command(["start"]) & ~filters.forwarded)
@app.on_edited_message(filters.command(["start"]) & ~filters.forwarded)
async def fallen_st(_, message: Message):
    if message.chat.type == ChatType.PRIVATE:
        upt = int(time.time() - StartTime)
        uptime = get_readable_time((upt))
        try:
            await message.reply_photo(
                photo=config.START_IMG,
                caption=PM_START_TEXT.format(
                    message.from_user.first_name,
                    BOT_NAME,
                    BOT_USERNAME,
                    uptime,
                ),
                reply_markup=InlineKeyboardMarkup(pm_buttons),
            )
        except Exception as ex:
            print(ex)
            await message.reply_text(
                text=PM_START_TEXT.format(
                    message.from_user.first_name,
                    BOT_NAME,
                    BOT_USERNAME,
                    uptime,
                ),
                reply_markup=InlineKeyboardMarkup(pm_buttons),
                disable_web_page_preview=True,
            )
    else:
        try:
            await message.reply_photo(
                photo=config.START_IMG,
                caption=START_TEXT.format(
                    message.from_user.first_name,
                    BOT_NAME,
                    BOT_USERNAME,
                    message.chat.title,
                    config.SUPPORT_CHAT,
                ),
                reply_markup=InlineKeyboardMarkup(gp_buttons),
            )
        except Exception as ex:
            print(ex)
            await message.reply_text(
                text=START_TEXT.format(
                    message.from_user.first_name,
                    BOT_NAME,
                    BOT_USERNAME,
                    message.chat.title,
                    config.SUPPORT_CHAT,
                ),
                reply_markup=InlineKeyboardMarkup(gp_buttons),
                disable_web_page_preview=True,
            )
