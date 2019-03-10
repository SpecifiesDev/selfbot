import discord
import asyncio
import time

client = discord.Client()
channelids = []
@client.event
async def on_ready():
    print('')
    print('ID: ',client.user.id)
    print('Discord version: ',discord.__version__)
    print('Servers connected to:')
    getIds()
    writeIds()
@client.event
async def on_message(message):
    if message.author == client.user:
        m = message.content
        channel = message.channel
        if "clear" in m:
            async for msg in client.logs_from(message.channel, limit = 10000):
                if msg.author == client.user:
                    try:
                        await client.delete_message(msg)
                    except:
                        pass
            await client.send_message(message.channel, "Messages deleted.")
        if "adminclear" in m:
            async for msg in client.logs_from(message.channel, limit = 10000):
                try:
                    await client.delete_message(msg)
                except:
                    pass
        if "silent" in m:
            toIndex = m.strip("clearsilent ")
            try:
                channel = client.get_channel(channelids[int(toIndex)])
                print("Starting the silent clearing of the DM with: " + channel.user.name)
                async for msg in client.logs_from(channel, limit = 10000):
                    if msg.author == client.user:
                        try:
                            await client.delete_message(msg)
                            print("Cleared message: '" + msg + "'")
                        except:
                            pass
            except:
                print('Usage: silent (index)')
def getIds():
    global channelids
    x = -1
    for ch in client.private_channels:
        x = x + 1
        channelids.append(ch.id)
def writeIds():
    file = open("clientids.txt", "w")
    global channelids
    x = -1
    for c in channelids:
        x = x + 1
        try:
            file.write(c + " (" + str(x) + ") - " + client.get_channel(c).user.name + "\n")
        except:
            pass
    file.write("The numbers are the list index. If any are skipped there were errors with grabbing their data.")
#Replace token with string version of your own discord token.
client.run(token , bot=False)
