import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!stalin'):
        await message.channel.send('https://tenor.com/view/joseph-stalin-soviet-gesture-cigar-gif-15512721')
    if message.content.startswith('!mykullcpr'):
        await message.channel.send('https://tenor.com/view/michael-reeves-cpr-mouth-to-mouth-fire-gif-20754258')
    if message.content.startswith('!mykullsax'):
        await message.channel.send('https://tenor.com/view/michael-michael-reeves-saxophone-music-gif-19814036')
    if message.content.startswith('!gay'):
        await message.channel.send('https://media1.tenor.com/images/6aeaadd18095ba812ba267dc9b188f72/tenor.gif?itemid=17057380')
    if message.content.startswith('!baka'):
        await message.channel.send('https://tenor.com/view/baka-anime-gif-12908346')
    if message.content.startswith('!gun'):
        await message.channel.send('https://tenor.com/view/iwin-easy-shooting-gun-shot-gun-gif-13437188')
client.run(os.environ['access'])