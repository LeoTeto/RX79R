from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from AarohiX import app

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not "https://t.me/WX_PM":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("WX_PM", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/WX_PM".isalpha():
                link = "https://t.me/WX_PM"
            else:
                chat_info = await bot.get_chat("WX_PM")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"**◇︰ اهـلا يا {msg.from_user.mention} الانضمام الى هذهِ القناة أولاً  \n◇︰ اشترك ثم أرسل :/start **",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("ᴍᴜꜱɪᴄ ᴜᴘᴅᴀᴛᴇᴅ", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I m not admin in the MUST_JOIN chat @WX_PM !")
      
