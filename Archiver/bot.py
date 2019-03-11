import discord
import asyncio
import time

client = discord.Client()


@client.event
async def on_ready():
    print('')
    print('ID: ',client.user.id)
    print('Discord version: ',discord.__version__)
    
@client.event
async def on_message(message):
    if str(message.channel.type) == "private":

        #get the author id
        aid = str(message.author)

        cid = str(message.channel.id)


        # Detecting if it's an image.
        try:
            url = message.attachments[0]['url']
            write(str(url), aid, cid)
        except:
            content = message.content
            write(content, aid, cid)
            

def write(content, author, cid):
    try:
        with open("./data/" + cid + ".txt", "a") as f:
            f.write(author + " >> " + content + "\n")
    except Exception as e:
        print(e)
    
                    
                
client.run("token" , bot=False)
