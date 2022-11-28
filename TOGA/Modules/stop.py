from pyrogram import filters
from pyrogram.types import Message

from TOGA import app, pytgcalls
from TOGA.Helpers import _clear_, close_key, admin_check


@app.on_message(filters.command(["stop", "end"]) & filters.group)
@admin_check
async def stop_str(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        await _clear_(message.chat.id)
        await pytgcalls.leave_group_call(message.chat.id)
    except:
        pass

    return await message.reply_text(
        text=f"• **sᴛʀᴇᴀᴍ ᴇɴᴅᴇᴅ/sᴛᴏᴩᴩᴇᴅ**•\n│ \n└ʙʏ : {message.from_user.mention}",
        reply_markup=close_key,
    )
