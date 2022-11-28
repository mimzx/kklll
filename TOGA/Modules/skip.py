from pyrogram import filters
from pyrogram.types import Message

from pytgcalls import StreamType
from pytgcalls.types import HighQualityAudio
from pytgcalls.types.input_stream import InputStream, InputAudioStream

from TOGA import app, pytgcalls, fallendb
from TOGA.Helpers import close_key, buttons, admin_check, _clear_, gen_thumb


@app.on_message(filters.command(["skip", "next"]) & filters.group)
@admin_check
async def skip_str(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    get = fallendb.get(message.chat.id)
    if not get:
        try:
            await _clear_(message.chat.id)
            await pytgcalls.leave_group_call(message.chat.id)
            await message.reply_text(
                text=f"➻ sᴛʀᴇᴀᴍ sᴋɪᴩᴩᴇᴅ \n│ \n└ʙʏ : {message.from_user.mention} \n\n**» ɴᴏ ᴍᴏʀᴇ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs ɪɴ** {message.chat.title}, **ʟᴇᴀᴠɪɴɢ ᴠɪᴅᴇᴏᴄʜᴀᴛ.**",
                reply_markup=close_key,
            )
        except:
            return
    else:
        title = get[0]["title"]
        duration = get[0]["duration"]
        file_path = get[0]["file_path"]
        videoid = get[0]["videoid"]
        req_by = get[0]["req"]
        get.pop(0)

        stream = InputStream(
            InputAudioStream(
                file_path,
                parameters=HighQualityAudio(),
            )
        )
        try:
            await pytgcalls.change_stream(
                message.chat.id,
                stream,
            )
        except:
            await _clear_(message.chat.id)
            return await pytgcalls.leave_group_call(message.chat.id)

        await message.reply_text(
            text=f"➻ sᴛʀᴇᴀᴍ sᴋɪᴩᴩᴇᴅ \n│ \n└ʙʏ : {message.from_user.mention} ",
            reply_markup=close_key,
        )
        img = await gen_thumb(videoid)
        return await message.reply_photo(
            photo=img,
            caption=f"**➻ sᴛᴀʀᴛᴇᴅ sᴛʀᴇᴀᴍɪɴɢ**\n\n **ᴛɪᴛʟᴇ :** {title[:27]}\n **ᴅᴜʀᴀᴛɪᴏɴ :** `{duration}` ᴍɪɴᴜᴛᴇs\n **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {req_by}",
            reply_markup=buttons,
        )
