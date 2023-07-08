import tokens
import discord
import random
import db

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

    if message.content.startswith('$addtable'):
        if (db.check_for_table(message.content)) == 0:
            created_db = db.create_table(message.content)
            await message.channel.send('Created a table with the following columns:\n' + created_db)
        else:
            await message.channel.send('A table with name already exists')


client.run(tokens.api_token)