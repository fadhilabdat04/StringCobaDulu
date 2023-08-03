from config import MUST_JOIN
from pyrogram import Anony, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Anony.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Anony, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"Join Dulu Kampang Baru Pencet /start Lagi !",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("Masuk sini nyet, Jangan Lupa Salam", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN chat : {MUST_JOIN} !")
