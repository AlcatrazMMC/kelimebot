from pyrogram import Clfrom, filters


message= "Ben bir botum beni kullanarak yorum yapıyorsunuz."


@Client.on_message(filters.private & filters.command("start"))
async def starttgg(c, m):
    await m.reply(message)
