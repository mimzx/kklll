from pyrogram import filters
from pyrogram.types import Message

from FallenMusic import app, pytgcalls
from FallenMusic.Helpers import close_key, admin_check, stream_off, is_streaming


@app.on_message(filters.command(["pause"]) & filters.group)
@admin_check
async def pause_str(_, message: Message):
    try:
        await message.delete()
    except:
        pass

    if not await is_streaming(message.chat.id):
        return await message.reply_text("ᴅɪᴅ ʏᴏᴜ ʀᴇᴍᴇᴍʙᴇʀ ᴛʜᴀᴛ ʏᴏᴜ ʀᴇsᴜᴍᴇᴅ ᴛʜᴇ sᴛʀᴇᴀᴍ ?")

    await pytgcalls.pause_stream(message.chat.id)
    await stream_off(message.chat.id)
    return await message.reply_text(
        text=f"➻ sᴛʀᴇᴀᴍ ᴩᴀᴜsᴇᴅ \n│ \n└ʙʏ : {message.from_user.mention}",
        reply_markup=close_key,
    )
