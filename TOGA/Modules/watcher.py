from pyrogram import filters
from pyrogram.types import Message

from pytgcalls import StreamType
from pytgcalls.types import Update, HighQualityAudio
from pytgcalls.exceptions import NoActiveGroupCall
from pytgcalls.types.input_stream import InputStream, InputAudioStream

from TOGA import app, app2, fallendb, pytgcalls, BOT_ID
from TOGA.Helpers import buttons, _clear_, gen_thumb

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    try:
        await _clear_(message.chat.id)
    except:
        pass
    try:
        await pytgcalls.leave_group_call(message.chat.id)
    except:
        pass


@app.on_message(filters.left_chat_member)
async def ub_leave(_, message: Message):
    if message.left_chat_member.id == BOT_ID:
        try:
            await _clear_(message.chat.id)
        except:
            pass
        try:
            await pytgcalls.leave_group_call(message.chat.id)
        except:
            pass
        try:
            await app2.leave_chat(message.chat.id)
        except:
            pass


@pytgcalls.on_stream_end()
async def on_stream_end(pytgcalls, update: Update):
    chat_id = update.chat_id

    get = fallendb.get(chat_id)
    if not get:
        try:
            await _clear_(chat_id)
            return await pytgcalls.leave_group_call(chat_id)
        except:
            return
    else:
        process = await app.send_message(
            chat_id=chat_id,
            text="» ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ɴᴇxᴛ ᴛʀᴀᴄᴋ ғʀᴏᴍ ᴏ̨ᴜᴇᴜᴇ...",
        )
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
                chat_id,
                stream,
            )
        except Exception as ex:
            print(ex)
            await _clear_(chat_id)
            return await pytgcalls.leave_group_call(chat_id)

        img = await gen_thumb(videoid)
        await process.delete()
        await app.send_photo(
            chat_id=chat_id,
            photo=img,
            caption=f"**• sᴛᴀʀᴛᴇᴅ sᴛʀᴇᴀᴍɪɴɢ**\n\n **• ᴛɪᴛʟᴇ :** {title[:27]}\n **• ᴅᴜʀᴀᴛɪᴏɴ :** `{duration}` ᴍɪɴᴜᴛᴇs\n **• ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {req_by}",
            reply_markup=buttons,
        )
