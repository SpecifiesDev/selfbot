import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('')
    print('ID: ',client.user.id)
    print('Discord version: ',discord.__version__)
    print('Servers connected to:')
    for server in client.servers:
        print(server.name)
@client.event
async def on_message(message):
    if message.author == client.user:
        m = message.content
        if "clear" in m:
            async for msg in client.logs_from(message.channel, limit = 10000):
                if msg.author == client.user:
                    try:
                        await client.delete_message(msg)
                    except Exception as e:
                        pass
            await client.send_message(message.channel, "Messages deleted.")
        if "adminclear" in m:
            async for msg in client.logs_from(message.channel, limit = 10000):
                try:
                    await client.delete_message(msg)
                except Exception as e:
                    pass


client.run(token , bot=False)
