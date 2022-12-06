# Voics Chatbot Module Credits Pranav Ajay 🐰Github = Red-Aura 🐹 Telegram= @madepranav
# @lyciachatbot support Now
import os

import aiofiles
import aiohttp
from pyrogram import filters

from Millie.services.pyrogram import pbot


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                data = await resp.json()
            except:
                data = await resp.text()
    return data


async def ai_pbot(url):
    ai_name = "Millie.mp3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(ai_name, mode="wb")
                await f.write(await resp.read())
                await f.close()
    return ai_name


@pbot.on_message(filters.command("Millie"))
async def pbot(_, message):
    if len(message.command) < 2:
        await message.reply_text("Millie AI Voice Chatbot")
        return
    text = message.text.split(None, 1)[1]
    pbot = text.replace(" ", "%20")
    m = await message.reply_text("Millie Is Best...")
    try:
        L = await fetch(
            f"https://api.affiliateplus.xyz/api/chatbot?message={pbot}&botname=Daisy&ownername=TeamDaisyX&user=1"
        )
        chatbot = L["message"]
        VoiceAi = f"https://lyciavoice.herokuapp.com/lycia?text={chatbot}&lang=hi"
        name = "Millie"
    except Exception as e:
        await m.edit(str(e))
        return
    await m.edit("Made By @madepranav...")
    pbotVoice = await ai_lycia(VoiceAi)
    await m.edit("Repyping...")
    await message.reply_audio(audio=pbotVoice, title=chatbot, performer=name)
    os.remove(pbotVoice)
    await m.delete()
