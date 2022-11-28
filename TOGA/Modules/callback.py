import time

from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup

from pytgcalls import StreamType
from pytgcalls.types import HighQualityAudio
from pytgcalls.types.input_stream import InputStream, InputAudioStream

from FallenMusic import (
    app,
    pytgcalls,
    fallendb,
    ASS_ID,
    ASS_NAME,
    BOT_ID,
    BOT_NAME,
    BOT_USERNAME,
    StartTime,
)
from FallenMusic.Helpers import admin_check_cb, _clear_, gen_thumb, stream_on, stream_off, is_streaming, get_readable_time
from FallenMusic.Helpers.dossier import *
from FallenMusic.Helpers.inline import (close_key, helpmenu, buttons,
                                        help_back, pm_buttons)


@app.on_callback_query(filters.regex("forceclose"))
async def forceclose_command(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    query, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        try:
            return await CallbackQuery.answer(
                "» ɪᴛ'ʟʟ ʙᴇ ʙᴇᴛᴛᴇʀ ɪғ ʏᴏᴜ sᴛᴀʏ ɪɴ ʏᴏᴜʀ ʟɪᴍɪᴛs ʙᴀʙʏ.", show_alert=True
            )
        except:
            return
    await CallbackQuery.message.delete()
    try:
        await CallbackQuery.answer()
    except:
        return


@app.on_callback_query(filters.regex(pattern=r"^(resume_cb|pause_cb|skip_cb|end_cb)$"))
@admin_check_cb
async def admin_cbs(_, query: CallbackQuery):
    data = query.matches[0].group(1)

    if data == "resume_cb":
        if await is_streaming(query.message.chat.id):
            return await query.answer("ᴅɪᴅ ʏᴏᴜ ʀᴇᴍᴇᴍʙᴇʀ ᴛʜᴀᴛ ʏᴏᴜ ᴘᴀᴜsᴇᴅ ᴛʜᴇ sᴛʀᴇᴀᴍ ?", show_alert=True)
        await stream_on(query.message.chat.id)
        await pytgcalls.resume_stream(query.message.chat.id)
        await query.message.reply_text(
            text=f"➻ sᴛʀᴇᴀᴍ ʀᴇsᴜᴍᴇᴅ\n│ \n└ʙʏ : {query.from_user.mention} ",
            reply_markup=close_key,
        )

    elif data == "pause_cb":
        if not await is_streaming(query.message.chat.id):
            return await query.answer("ᴅɪᴅ ʏᴏᴜ ʀᴇᴍᴇᴍʙᴇʀ ᴛʜᴀᴛ ʏᴏᴜ ʀᴇsᴜᴍᴇᴅ ᴛʜᴇ sᴛʀᴇᴀᴍ ?", show_alert=True)
        await stream_off(query.message.chat.id)
        await pytgcalls.pause_stream(query.message.chat.id)
        await query.message.reply_text(
            text=f"➻ sᴛʀᴇᴀᴍ ᴩᴀᴜsᴇᴅ\n│ \n└ʙʏ : {query.from_user.mention} ",
            reply_markup=close_key,
        )

    elif data == "end_cb":
        try:
            await _clear_(query.message.chat.id)
            await pytgcalls.leave_group_call(query.message.chat.id)
        except:
            pass
        await query.message.reply_text(
            text=f"➻ sᴛʀᴇᴀᴍ ᴇɴᴅᴇᴅ/sᴛᴏᴩᴩᴇᴅ\n│ \n└ʙʏ : {query.from_user.mention} ",
            reply_markup=close_key,
        )
        await query.message.delete()

    elif data == "skip_cb":
        get = fallendb.get(query.message.chat.id)
        if not get:
            try:
                await _clear_(query.message.chat.id)
                await pytgcalls.leave_group_call(query.message.chat.id)
                await query.message.reply_text(
                    text=f"➻ sᴛʀᴇᴀᴍ sᴋɪᴩᴩᴇᴅ\n│ \n└ʙʏ : {query.from_user.mention}\n\n**» ɴᴏ ᴍᴏʀᴇ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs ɪɴ** {query.message.chat.title}, **ʟᴇᴀᴠɪɴɢ ᴠɪᴅᴇᴏᴄʜᴀᴛ.**",
                    reply_markup=close_key,
                )
                return await query.message.delete()
            except:
                return
        else:
            title = get[0]["title"]
            duration = get[0]["duration"]
            videoid = get[0]["videoid"]
            file_path = get[0]["file_path"]
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
                    query.message.chat.id,
                    stream,
                )
            except Exception as ex:
                print(ex)
                await _clear_(query.message.chat.id)
                return await pytgcalls.leave_group_call(query.message.chat.id)

            img = await gen_thumb(videoid)
            await query.edit_message_text(
                text=f"➻ sᴛʀᴇᴀᴍ sᴋɪᴩᴩᴇᴅ\n│ \n└ʙʏ : {query.from_user.mention}",
                reply_markup=close_key,
            )
            return await query.message.reply_photo(
                photo=img,
                caption=f"**➻ sᴛᴀʀᴛᴇᴅ sᴛʀᴇᴀᴍɪɴɢ**\n\n **ᴛɪᴛʟᴇ :** {title[:27]}\n **ᴅᴜʀᴀᴛɪᴏɴ :** `{duration}` ᴍɪɴᴜᴛᴇs\n **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {req_by}",
                reply_markup=buttons,
            )


@app.on_callback_query(filters.regex("unban_ass"))
async def unban_ass(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    chat_id, user_id = callback_request.split("|")
    umm = (await app.get_chat_member(int(chat_id), BOT_ID)).privileges
    if umm.can_restrict_members:
        try:
            await app.unban_chat_member(int(chat_id), ASS_ID)
        except:
            return await CallbackQuery.answer(
                "» ғᴀɪʟᴇᴅ ᴛᴏ ᴜɴʙᴀɴ ᴀssɪsᴛᴀɴᴛ.",
                show_alert=True,
            )
        return await CallbackQuery.edit_message_text(
            f"➻ {ASS_NAME} sᴜᴄᴄᴇssғᴜʟʟʏ ᴜɴʙᴀɴɴᴇᴅ ʙʏ {CallbackQuery.from_user.mention}.\n\nᴛʀʏ ᴘʟᴀʏɪɴɢ ɴᴏᴡ..."
        )
    else:
        return await CallbackQuery.answer(
                "» ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴs ᴛᴏ ᴜɴʙᴀɴ ᴜsᴇʀs ɪɴ ᴛʜɪs ᴄʜᴀᴛ.",
                show_alert=True,
            )


@app.on_callback_query(filters.regex("fallen_help"))
async def help_menu(_, query: CallbackQuery):
    try:
        await query.answer()
    except:
        pass

    try:
        await query.edit_message_text(
            text=f"๏ ʜᴇʏ {query.from_user.first_name}, \n\nᴘʟᴇᴀsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴘ.",
            reply_markup=InlineKeyboardMarkup(helpmenu),
        )
    except Exception as e:
        print(e)
        return


@app.on_callback_query(filters.regex("close"))
async def del_qu(_, query: CallbackQuery):
    try:
        await query.message.delete()
    except:
        pass


@app.on_callback_query(filters.regex("fallen_cb"))
async def open_hmenu(_, query: CallbackQuery):
    callback_data = query.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup(help_back)

    try:
        await query.answer()
    except:
        pass

    if cb == "help":
        await query.edit_message_text(
            HELP_TEXT, reply_markup=keyboard
        )
    elif cb == "sudo":
        await query.edit_message_text(
            HELP_SUDO, reply_markup=keyboard
        )
    elif cb == "owner":
        await query.edit_message_text(
            HELP_DEV, reply_markup=keyboard
        )


@app.on_callback_query(filters.regex("fallen_home"))
async def home_fallen(_, query: CallbackQuery):
    upt = int(time.time() - StartTime)
    uptime = get_readable_time((upt))
    try:
        await query.answer()
    except:
        pass
    try:
        await query.edit_message_text(
            text=PM_START_TEXT.format(
                query.from_user.first_name,
                BOT_NAME,
                BOT_USERNAME,
                uptime,
            ),
            reply_markup=InlineKeyboardMarkup(pm_buttons),
        )
    except:
        pass
