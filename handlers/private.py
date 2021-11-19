from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAItmWD3OC0m03OLIcpSzfiJMCDxm4xJAAKFAwACH8C5V-U9VextES_XIAQ")
    await message.reply_text(
       f"""**مرحبا 🙋 _ {bn} 🎀
انا بوت تشغيل الموسيقه ف المحادثات الصوتيه قناه البوت https://t.me/U_5G_U!**

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᗪᗴᐯᗴᒪOᑭᗴᖇՏ", url="https://t.me/DEV_DEMONIC" )
                  ],[
                    InlineKeyboardButton(
                        "للـمـسـاعـده", url="https://t.me/T_elgram"
                    ),
                    InlineKeyboardButton(
                        "قـنـاة الـبـوت", url="https://t.me/U_5G_U"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "اضـف الـبـوت لـمـجـمـوعـتـك", url="https://t.me/PX6Jbot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Yes iᴍ online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📟Uᴩᴅᴀᴛᴇs", url="https://t.me/U_5G_U")
                ]
            ]
        )
   )
