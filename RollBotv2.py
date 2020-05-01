import nest_asyncio
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '/')
token = 'NjUwNjI2NDk5OTU4OTMxNDc2.Xf09cQ.rtDAsC5iPLnq19NwjjYNqZMI25o'
nest_asyncio.apply()

@client.event
async def on_message(message):
    m = message.content
    u = message.author.name
    if m == '/roll':
        await message.channel.send(u + ' rolls ' + str(random.randint(1,100)) 
        + ' (1-100)')
        return
    else: listmessage = m.split()
    if listmessage[0] == '/roll': 
        if isinstance(int(listmessage[1]), int):
            numberstr = listmessage[1]
        
            await message.channel.send((u + ' rolls ' 
                                        + str(random.randint(1,int(numberstr))) 
                                        + ' (1-' + str(int(numberstr)) + ')'))


client.run(token)





