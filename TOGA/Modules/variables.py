from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums import ChatType

import config
from TOGA import app, BOT_NAME, OWNER


@app.on_message(filters.command(["config", "variables"]) & filters.user(OWNER))
async def get_vars(_, message: Message):
    try:
        await app.send_message(
            chat_id=int(OWNER),
            text = f"""<u>**{BOT_NAME} ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs :**</u>

**ᴀᴘɪ_ɪᴅ :** `{config.API_ID}`
**ᴀᴘɪ_ʜᴀsʜ :** `{config.API_HASH}`

**ʙᴏᴛ_ᴛᴏᴋᴇɴ :** `{config.BOT_TOKEN}`
**ᴅᴜʀᴀᴛɪᴏɴ_ʟɪᴍɪᴛ :** `{config.DURATION_LIMIT}`

**ᴏᴡɴᴇʀ_ɪᴅ :** `{config.OWNER_ID}`
**sᴜᴅᴏ_ᴜsᴇʀs :** `{config.SUDO_USERS}`

**ᴘɪɴɢ_ɪᴍɢ :** `{config.PING_IMG}`
**sᴛᴀʀᴛ_ɪᴍɢ :** `{config.START_IMG}`
**sᴜᴘᴘᴏʀᴛ_ᴄʜᴀᴛ :** `{config.SUPPORT_CHAT}`

**sᴇssɪᴏɴ :** `{config.SESSION}`""",
            disable_web_page_preview=True,
        )
    except Exception as ex:
        print(ex)
        return await message.reply_text("» ғᴀɪʟᴇᴅ ᴛᴏ sᴇɴᴅ ᴛʜᴇ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs.")
    if message.chat.type != ChatType.PRIVATE:
        await message.reply_text("» ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘᴍ, ɪ'ᴠᴇ sᴇɴᴛ ᴛʜᴇ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs ᴛʜᴇʀᴇ.")
