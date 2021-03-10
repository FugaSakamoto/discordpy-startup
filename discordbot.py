import random
import asyncio #sleepを使うのに必要
import discord ##discordでBOTを使うのにこれが必ずいる

if message.content == "スロット":
kakuritu = random.randint(1, 199)
slot_list = [':8_1:', ':8_2:', ':8_3:', ':8_4:', ':8_5:', ':8_6:', ':8_7:']
A = random.choice(slot_list)
B = random.choice(slot_list)
C = random.choice(slot_list)
if int(kakuritu) == int(1): #確率は1 /399
await client.send_message(message.channel, "ボーナス確定！！！")
await asyncio.sleep(3) #3秒間待ってやる
await client.send_message(message.channel, ':seven:', ':seven:', ':seven:') #7だけ出るように指定
else:
await client.send_message(message.channel, "%s%s%s" % (A, B, C))
