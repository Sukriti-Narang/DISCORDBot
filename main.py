
import discord
import os
import requests
import json
import random
from dotenv import load_dotenv
from discord.ext import commands

bot = commands.Bot(command_prefix="$",intents=discord.Intents.default())



load_dotenv()

client = discord.Client(intents=discord.Intents.default())

def get_quote():

  SUKRITI_quotes=["You can do it :)"," Ups in life come after downs","When the going gets tough, the tough gets going !"]
  response = random.choice(SUKRITI_quotes)

  return(quote)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
#REPLY FOR HIII
    if msg.startswith('$hiii'):
        await message.channel.send('Heyy there welcome to sukriti bot :) ')

  #INCASE YOU NEED MOTIVATION , WE GIVE YOU ENCOURAGING MSGS 
    if msg.startswith('$motivate'):
      encourage_msg = response = random.choice(get_quotes())
      await message.channel.send(encourage_msg)


    bad_words = ["hell", "die", "suck", "loser"]

    starter_encouragements = [
  "Warning! Ban", "These actions can lead you to get banned"
]

#YOU MIGHT GET A BAN IF YOU USE BAD WORDS
    if any(word in msg for word in bad_words):
      await message.channel.send(random.choice(starter_encouragements))
    

#client.run('MTA0NDIwNDkwMDgxODYzMjc4NQ.G4KWRg.KAklR-BSEE_Sa__6npjzYbpsRdrHub-fkzus


#USE print COMMAND IN BOT TO PRINT ANYTHING
@bot.command()
async def print(ctx, *msgs):
	reply = ""

	for msg in msgs:
		reply = reply + " " + msg

	await ctx.channel.send(reply)



#PLAY A DICE GAME
@bot.command(name='lucky_number')
async def roll(ctx, Date_Of_Birth: int):
    luck = [
        str(random.choice(range(Date_Of_Birth,Date_Of_Birth + 7)))
        for _ in range(Date_Of_Birth)
    ]
    await ctx.send(', '.join(luck))



#CREATE A NEW CHANNEL IF YOU ARE ADMIN
@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='SukritiBot'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')
      
my_secret = os.environ['TOKEN']

#client.run('my_secret')
#client.run(os.getenv('my_secret'))
