import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('hello'):
    await message.channel.send('hello to you too!')
  if message.content.startswith('what the fuck'):
    await message.channel.send('Use of inappropriate word')
  if message.content.startswith('wtf'):
    await message.channel.send('Use of inappropriate word')
  if message.content.startswith('bitch'):
    await message.channel.sent('use of inappropriate word')
  if message.content.startswith('bitch'):
    await message.channel.sent('use of inappropriate word')

client.run(os.getenv('TOKEN'))
