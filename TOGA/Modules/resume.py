from pyrogram import filters
from pyrogram.types import Message

from TOGA import app, pytgcalls
from TOGA.Helpers import close_key, admin_check, stream_on, is_streaming


@app.on_message(filters.command(["resume"]) & filters.group)
@admin_check
async def res_str(_, message: Message):
    try:
        await message.delete()
    except:
        pass

    if await is_streaming(message.chat.id):
        return await message.reply_text("ᴅɪᴅ ʏᴏᴜ ʀᴇᴍᴇᴍʙᴇʀ ᴛʜᴀᴛ ʏᴏᴜ ᴘᴀᴜsᴇᴅ ᴛʜᴇ sᴛʀᴇᴀᴍ ?")
    await stream_on(message.chat.id)
    await pytgcalls.resume_stream(message.chat.id)
    return await message.reply_text(
        text=f"➻ sᴛʀᴇᴀᴍ ʀᴇsᴜᴍᴇᴅ \n│ \n└ʙʏ : {message.from_user.mention} ",
        reply_markup=close_key,
    )
