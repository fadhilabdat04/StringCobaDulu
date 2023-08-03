from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="Ambil String Disini", callback_data="gensession")],
        [
            InlineKeyboardButton(text="Support", url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text="🚀 Jasa Si Arab", url="https://t.me/SiArab_Store"
            ),
        ],
        [
            InlineKeyboardButton(text="🥷🏻 Pemilik Bot", url="https://t.me/Arabnihnge"),
            InlineKeyboardButton(
                text="💰 Donasi", url="https://telegra.ph//file/f7f455a01060b767d4781.jpg"
            ),
        ],
         [
            InlineKeyboardButton(
                text="➕ Tambahkan Saya Menjadi Di GC Ampas-mu ➕",
                url=f"http://t.me/{BOT_USERNAME}?startgroup=new",
            )
        ],
    ]
)
       
gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="ᴛʀʏ ᴀɢᴀɪɴ", callback_data="gensession")]]
)
