import discord

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
        await message.channel.send('https://tenor.com/view/them-old-gay-boys-leslie-jordan-cameo-gay-gay-boys-gif-17826781')
    if message.content.startswith('!baka'):
        await message.channel.send('https://tenor.com/view/baka-anime-gif-12908346')
    if message.content.startswith('!gun'):
        await message.channel.send('https://tenor.com/view/iwin-easy-shooting-gun-shot-gun-gif-13437188')
client.run("ODQ4MTgwNDM4MDgyMjU2OTE2.YLI3lg.PSqossuxJESaJzQZ5YxdX7uQI-k")