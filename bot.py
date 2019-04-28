import discord
from discord.ext import commands
client = commands.Bot(command_prefix = '*')
@client.event
async def on_ready() :
    print('Bot is ready')

@client.event
async def on_message(message) :
    sent = message.content
    id = client.get_guild(544099615268667402)
    if message.content.find('*ping') != -1:
        await message.channel.send('pong')
client.run(str(os.environ.get('BOT_TOKEN')))
