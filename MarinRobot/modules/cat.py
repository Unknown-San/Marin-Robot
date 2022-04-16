from pyrogram import filters

from MarinRobot import pbot as app
from MarinRobot.utils.errors import capture_err




@app.on_message(filters.command("wsfw"))
@capture_err
async def take_ss(_, message):
    try:
        if len(message.command) != 2:
            await message.reply_text("Give A Query Meow!.")
            return
        url = message.text.split(None, 1)[1]
        m = await message.reply_text("Taking Screenshot")
        await m.edit("Uploading")
        try:
            await app.send_photo(
                message.chat.id,
                photo=f"https://api.waifu.pics/sfw/{url}",
            )
        except TypeError:
            await m.edit("No Response Meow!.")
            return
        await m.delete()
    except Exception as e:
        await message.reply_text(str(e))
