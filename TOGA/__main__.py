import os
import asyncio
import importlib

from pyrogram import idle
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioVideoPiped

from .logging import LOGGER
from FallenMusic import (app, app2, pytgcalls, SUNAME,
                         BOT_ID, BOT_NAME, BOT_USERNAME,
                         ASS_ID, ASS_NAME, ASS_USERNAME)
from FallenMusic.Modules import ALL_MODULES


async def fallen_startup():
    LOGGER("FallenMusic").info("[•] Loading Modules...")
    for module in ALL_MODULES:
        importlib.import_module("FallenMusic.Modules." + module)
    LOGGER("FallenMusic").info(f"[•] Loaded {len(ALL_MODULES)} Modules.")

    LOGGER("FallenMusic").info("[•] Refreshing Directories...")
    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")
    if "raw_files" not in os.listdir():
        os.mkdir("raw_files")
    LOGGER("FallenMusic").info("[•] Directories Refreshed.")

    try:
        await app.send_message(SUNAME, f"✯ ғᴀʟʟᴇɴ ᴍᴜsɪᴄ ʙᴏᴛ ✯\n\n𖢵 ɪᴅ : `{BOT_ID}`\n𖢵 ɴᴀᴍᴇ : {BOT_NAME}\n𖢵 ᴜsᴇʀɴᴀᴍᴇ : @{BOT_USERNAME}")
    except:
        LOGGER("FallenMusic").error(f"{BOT_NAME} failed to send message at @{SUNAME}, please go & check.")

    try:
        await app2.send_message(SUNAME, f"✯ ғᴀʟʟᴇɴ ᴍᴜsɪᴄ ᴀss ✯\n\n𖢵 ɪᴅ : `{ASS_ID}`\n𖢵 ɴᴀᴍᴇ : {ASS_NAME}\n𖢵 ᴜsᴇʀɴᴀᴍᴇ : @{ASS_USERNAME}")
    except:
        LOGGER("FallenMusic").error(f"{ASS_NAME} failed to send message at @{SUNAME}, please go & check.")

    LOGGER("FallenMusic").info(f"[•] Bot Started As {BOT_NAME}.")
    LOGGER("FallenMusic").info(f"[•] Assistant Started As {ASS_NAME}.")

    LOGGER("FallenMusic").info("[•] \x53\x74\x61\x72\x74\x69\x6e\x67\x20\x50\x79\x54\x67\x43\x61\x6c\x6c\x73\x20\x43\x6c\x69\x65\x6e\x74\x2e\x2e\x2e")
    await pytgcalls.start()
    try:
        await pytgcalls.join_group_call(
            -1001686672798,
            AudioVideoPiped("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"),
            stream_type=StreamType().pulse_stream,
        )
        await asyncio.sleep(11)
        await pytgcalls.leave_group_call(-1001686672798)
    except:
        pass
    await idle()


loop = asyncio.get_event_loop()

if __name__ == "__main__":
    loop.run_until_complete(fallen_startup())
    LOGGER("FallenMusic").error("Fallen Music Bot Stopped.")
