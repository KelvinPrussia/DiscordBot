import discord
import random


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        if message.author.global_name == "redraddishspirit":
            await message.channel.send('Hello smelly!')
        else:
            await message.channel.send('Hello my Lord!')
    
    if message.content.startswith('$choose'):
        turn = random.randint(1,2)
        if turn == 1:
            await message.channel.send('Aliyah\'s turn')
        else:
            await message.channel.send('Kelvin\'s turn')
    
    if message.content.startswith('$most_played'):
        temp = 1

client.run('token')