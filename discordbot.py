
import discord
import random
import asyncio
import os
import traceback

TOKEN = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_ready():
    await message.channel.send("Pフィーバー戦姫絶唱シンフォギア2 起動しました")

@client.event
async def on_message(message):
    if message.content.startswith("🎰"):
        kakuritu = random.randint(1, 199)
        slot_list = [":8_1:", ":8_2:", ":8_3:", ":8_4:", ":8_5:", ":8_6:", ":8_7:"]
        A = random.choice(slot_list)
        B = random.choice(slot_list)
        C = random.choice(slot_list)
        if int(kakuritu) == int(1):
            await message.channel.send(":9_letter:")
            await asyncio.sleep(3)
            await message.channel.send(":8_7:", ":8_7:", ":8_6:")
            await asyncio.sleep(1)
            await message.channel.send(":9_frieze:")
            await message.channel.send("ｶﾞﾄｩﾗﾝﾃﾞｨｽﾊﾞｰﾍﾞﾙｼﾞｰｸﾞﾚｯﾄｴｰﾃﾞﾙﾅｰｰﾙ…ｴﾐｭｽﾄｰﾛﾝｾﾞﾝﾌｨｰﾈｴﾙﾊﾞﾗｰｽﾞｨｰ…")
            await asyncio.sleep(3)
            await message.channel.send("ﾎﾟﾎﾟﾎﾟﾎﾟﾎﾟﾎﾟﾎﾟﾎﾟﾎﾟﾎﾟﾎﾟ!!ﾋﾟﾛﾋﾟﾛﾋﾟﾛﾋﾟﾛﾋﾟﾛﾋﾟﾛ!ﾋﾟﾛﾛﾛﾛﾛﾛﾛﾛﾛﾛﾛﾛ！ﾌﾞｩｰｰｰｳ↑ﾌﾞｩｰｰｰｳ↑ﾌﾞｩｰｰｰｳ↑")
            await asyncio.sleep(3)
            await message.channel.send(":9_symphogear:")
            await asyncio.sleep(3)
            await message.channel.send(":8_7:', ':8_7:', ':8_7:")
            return
        else:
            await message.channel.send("%s%s%s" % (A, B, C))
            return

client.run(TOKEN)
