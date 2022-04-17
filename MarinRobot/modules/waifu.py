import aiohttp
from pyrogram import filters
from MarinRobot import pbot
from MarinRobot.utils.errors import capture_err

@pbot.on_message(filters.command('random'))
@capture_err
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("Query Required")
        return
    query = message.text.split(None, 1)[1]
    URL = f'https://api.waifu.im/random/?selected_tags={query}'
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()
            try:

                source = result['source']

                avatar_url = result['url']
                description = result['description']
                tags = result['tags']
                source = result['source']
                caption = f"""**Mod by @XtheAnonymous**
**description:** `{description}`
**Tags:** `{tags}`

"""
            except Exception as e:
                print(str(e))
                pass
    await message.reply_photo(photo=avatar_url, caption=caption)
