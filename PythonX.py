# ©ItzExStar

import re
import aiohttp

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "5872061153:AAG94E59a4QQYiFAwNbw9hZvUD7JAS-KKtI"
USERS_API = {}

Altron = Client('XShortener',
            api_id=18136872,
            api_hash="312d861b78efcd1b02183b2ab52a83a4",
            bot_token=BOT_TOKEN,
            workers=100
            )

print("\n𝐃𝐞𝐩𝐥𝐨𝐲𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 😎🤘🏻\nMy Master ---> @𝐈𝐭𝐳𝐄𝐱𝐒𝐭𝐚𝐫")


@Altron.on_message(filters.command('start') & filters.private)
async def start(_, message):
    TEXT = """
🤖 **ʜᴇʏᴀ..!!! 
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ __ɪ'ᴍ ᴀ ʟɪɴᴋ ꜱʜᴏʀᴛᴇɴᴇʀ ʙᴏᴛ. ꜱᴇɴᴅ ᴍᴇ ʟɪɴᴋ ᴀɴᴅ ɪ'ʟʟ ɢɪᴠᴇ ʏᴏᴜ ʙᴀᴄᴋ ɪᴛ'ꜱ ꜱʜᴏʀᴛᴇɴᴇᴅ ʟɪɴᴋ__.
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
**⚠️ ʙʏ ᴅᴇꜰᴀᴜʟᴛ EᴀsʏSᴋʏ'ꜱ ᴀᴘɪ ᴋᴇʏ ᴀɴᴅ ᴀᴘɪ ᴜʀʟ ᴀʀᴇ ᴜꜱᴇᴅ !**
✘ ᴜꜱᴇ /help ᴛᴏ ɢᴇᴛ ᴍᴏʀᴇ sɪᴛᴇs ᴀᴘɪ ᴜʀʟ ᴀɴᴅ ᴀᴘɪ ᴋᴇʏ ℹ️.
"""
    await message.reply_photo(
        photo="https://te.legra.ph/file/ba44ebf64af97947a867b.jpg",
        caption=TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("✘ ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/ItzExStar"),
            ],
            [
                InlineKeyboardButton("✘ ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/AltronChats"),
                InlineKeyboardButton("✘ ᴄʜᴀɴɴᴇʟ", url="https://t.me/TheAltron"),
            ],
            ]     
        )
    )
    USERS_API[message.chat.id] = {"API_KEY":"https://easysky.in/members/tools/api", "API_URL":"https://easysky.in/api"}


@Altron.on_message(filters.command('help') & filters.private)
async def help(_, message):
    HELP_TEXT = f"""
**ᴀᴘɪ ᴜʀʟ ᴏꜰ ꜱᴏᴍᴇ ꜱɪᴛᴇꜱ ᴀʀᴇ:**

➲ **EasySky**
  ‣ ᴀᴘɪ ᴜʀʟ: https://easysky.in/api
  ‣ ᴀᴘɪ ᴋᴇʏ: https://easysky.in/members/tools/api

➲ **Droplink**
  ‣ ᴀᴘɪ ᴜʀʟ: https://droplink.co/api
  ‣ ᴀᴘɪ ᴋᴇʏ: https://droplink.co/member/tools/api

➲ **MdiskShortener**
  ‣ ᴀᴘɪ ᴜʀʟ: https://mdiskshortner.link/api
  ‣ ᴀᴘɪ ᴋᴇʏ: https://mdiskshortner.link/member/tools/api

➲ **DuLink**
  ‣ ᴀᴘɪ ᴜʀʟ: https://dulink.in/api
  ‣ ᴀᴘɪ ᴋᴇʏ: https://dulink.in/member/tools/api

➲ **GPLink**
  ‣ ᴀᴘɪ ᴜʀʟ: https://gplinks.in/api
  ‣ ᴀᴘɪ ᴋᴇʏ: https://gplinks.in/member/tools/api

➲ **PdiskShortener**
  ‣ ᴀᴘɪ ᴜʀʟ: https://pdiskshortener.com/api
  ‣ ᴀᴘɪ ᴋᴇʏ: https://pdiskshortener.com/member/tools/api

➲ **TnLink**
  ‣ ᴀᴘɪ ᴜʀʟ: https://tnlink.in/api
  ‣ ᴀᴘɪ ᴋᴇʏ: https://tnlink.in/member/tools/api

➲ **ClickyFly**
  ‣ ᴀᴘɪ ᴜʀʟ: https://clickyfly.com/api
  ‣ ᴀᴘɪ ᴋᴇʏ: https://clickyfly.com/member/tools/api


 ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ sᴇᴛ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴀᴘɪ ᴋᴇʏ ᴀɴᴅ ᴜʀʟ:
  ➲ /key <ᴀᴘɪ ᴋᴇʏ>: ᴛᴏ ᴜsᴇ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴀᴘɪ ᴋᴇʏ
  ➲ /url <ᴀᴘɪ ᴜʀʟ>: ᴛᴏ ᴜsᴇ ʏᴏᴜʀ ᴄᴜsᴛᴏᴍ ᴀᴘɪ ᴜʀʟ
"""
    await message.reply_text(HELP_TEXT)


@Altron.on_message(filters.command('key') & filters.private)
async def key(_, message):
  Key = message.text.split(" ")
  if len(Key) == 1:
    message.reply_text("» 𝗨𝘀𝗮𝗴𝗲: /key <ᴀᴘɪ ᴋᴇʏ>")
    return
  global USERS_API
  USERS_API[message.chat.id]["API_KEY"] = Key[1]
  await message.reply_text("» ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴀᴘɪ ᴋᴇʏ ʜᴀꜱ ʙᴇɴ ꜱᴇᴛᴇᴅ.")


@Altron.on_message(filters.command('url') & filters.private)
async def url(_, message):
  Url = message.text.split(" ")
  if len(Url) == 1:
    message.reply_text("» 𝗨𝘀𝗮𝗴𝗲: /url <ᴀᴘɪ ᴜʀʟ>")
    return
  global USERS_API
  USERS_API[message.chat.id]["API_URL"] = Url[1]
  await message.reply_text("» ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴀᴘɪ ᴜʀʟ ʜᴀꜱ ʙᴇɴ ꜱᴇᴛᴇᴅ.")


@Altron.on_message(filters.private & filters.text & filters.incoming)
async def link_handler(_, message):
    link_pattern = re.compile('https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}', re.DOTALL)
    links = re.findall(link_pattern, message.text)
    if len(links) < 1:
        await message.reply("» ɴᴏ ʟɪɴᴋꜱ ꜰᴏᴜɴᴅ ɪɴ ᴛʜɪꜱ ᴛᴇxᴛ.", quote=True)
        return
    for link in links:
        try:
            short_link = await get_shortlink(link, message.chat.id)
            await message.reply(f"» ʜᴇʀᴇ ɪꜱ ʏᴏᴜʀ ꜱʜᴏʀᴛᴇɴᴇᴅ ʟɪɴᴋ\n\n**ᴏʀɪɢɪɴᴀʟ ʟɪɴᴋ:** {link}\n**ꜱʜᴏʀᴛᴇɴᴇᴅ ʟɪɴᴋ:** `{short_link}`", quote=True, disable_web_page_preview=True)
        except Exception as e:
            await message.reply(f'ᴇʀʀᴏʀ: `{e}`', quote=True)


async def get_shortlink(link, ID):
    url = USERS_API[ID]["API_URL"]
    params = {'api': USERS_API[ID]["API_KEY"], 'url': link}
    print(url, params)

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, raise_for_status=True) as response:
            data = await response.json()
            return data["shortenedUrl"]

Altron.run()
