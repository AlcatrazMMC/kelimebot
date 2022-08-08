from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕ Məni qrupuna əlavə et", url=f"http://t.me/AlcatrazSozBot?startgroup=new")
    ],
    [
        InlineKeyboardButton("👨🏻‍💻 Sahib", url="t.me/OldDictator"),
        InlineKeyboardButton("✅ Rəsmi", url="t.me/AlzResmi"),
    ]
])


START = """
**Salam🗽, Alcatraz söz oyununa xoş gəldiniz. Vaxtınızı mənimlə əyləncəli keçirə bilərsiniz ✨..**
Əmrlər asanddır. 
"""

HELP = """
**🛠️ Əmrlər menyusuna xoş gəldiniz 🛠️.**
/soz - Söz oyunu başladar.
/oyred - Söz oyununda öyrədici olmaq.. 
/puan - Oyunçular arasındakı rəqabət məlumatı..


/game - Söz oyunu başladar.. 
/pass - Sözü pass keçər.
/skor - Oyunçular arasındakı rəqabət məlumatı..
/cancel Oyunu dayandırar.
"""

# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://telegra.ph/file/d515a91bead7784328772.jpg",caption=START,reply_markup=keyboard)

@Client.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://telegra.ph/file/3a177f6d7b5b5a3d0548f.jpg",caption=HELP) 

# Oyunu başlat. 
@Client.on_message(filters.command("game")) 
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**❗ Hal-hazırda qrupda oyun davam edir ✍🏻 \n Oyunu dayandırmaq üçün /cancel yazın")
    else:
        await m.reply(f"**{m.from_user.mention}** tərəfindən! \nSöz oyunu başladı .\n\nBol şanslar !", reply_markup=kanal)
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["pass"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/60 
📝 Söz :   <code>{kelime_list}</code>
💰 Qazandığınız xal: 1
🔎 İpucu: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {int(len(kelime_list)/2)} 

✏️ Qarışıq sözlərdən ibarət sözü tapın 
        """
        await c.send_message(m.chat.id, text)
        
