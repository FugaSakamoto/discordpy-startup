
from discord.ext import commands
import random
import asyncio
import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith("🎰"):
        kakuritu = random.randint(1, 199)
        slot_list = [':8_1:', ':8_2:', ':8_3:', ':8_4:', ':8_5:', ':8_6:', ':8_7:']
        A = random.choice(slot_list)
        B = random.choice(slot_list)
        C = random.choice(slot_list)
        if int(kakuritu) == int(1):
            await client.send_message(message.channel, ":9_letter:")
            await asyncio.sleep(3)
            await client.send_message(message.channel, ':8_7:', ':8_7:', ':8_7:')
            await asyncio.sleep(3)
            await client.send_message(message.channel, ':9_frieze:')
            await asyncio.sleep(3)
            await client.send_message(message.channel, ':9_symphogear:')
            return
        else:
            await client.send_message(message.channel, "%s%s%s" % (A, B, C))
            return

client.run(token)
