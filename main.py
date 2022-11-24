# #MTA0NDIwNDkwMDgxODYzMjc4NQ.GAOpKZ.bvJkJKiJeU8tO_0tMYMmt1-rX5q60YWgOWjGqo
# # bot.py



import discord
import os
import requests
import json
import random
from dotenv import load_dotenv
from discord.ext import commands
import discord
from discord import Member
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
#intents = discord.Intents(messages=True)
#client = discord.Client(intents=intents)



# intents = discord.Intents.all()
# client = discord.Client(intents=intents)

# #load_dotenv()


# client = discord.Client(intents=discord.Intents.all())
client = commands.Bot(command_prefix='!')
#client=discord.Client()

# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')
#     await client.process_commands(message="Go")
# @client.event
# async def on_message(ctx):
#     await ctx.send("HEY THERE !")



@client.event
async def on_message(message):
	username = str(message.author).split("#")[0]
	channel = str(message.channel.name)
	user_message = str(message.content)

	#print(f'Message {user_message} by {username} on {channel}')

	if message.author == client.user:
		return

	if channel == "random":
		if user_message.lower() == "hello":
			await message.channel.send(f'Hello {username}, "Welcome to sukriti bot')
			return
		elif user_message.lower() == "bye":
			await message.channel.send(f'Bye {username}')
		elif user_message.lower() == "motivate":
			jokes = ["You got this !", " When going get's tough, the tough gets going","Coffee and Productivity !"]
			await message.channel.send(random.choice(jokes))
		elif user_message.lower() == "die" or user_message.lower() == "suck":
			await message.channel.send(f"{message.author.mention} Message contains  a banned word.")
	await client.process_commands(message)


@client.command(
	# ADDS THIS VALUE TO THE $HELP PRINT MESSAGE.
	help="Looks like you need some help.",
	# ADDS THIS VALUE TO THE $HELP MESSAGE.
	brief="Prints the list of values back to the channel."
)
async def say(ctx, *abs):
	ans = ""
	ans=ans+" You say - "
	# LOOPS THROUGH THE LIST OF ARGUMENTS THAT THE USER INPUTS.
	for ab in abs:
		ans = ans + " " + ab

	# SENDS A MESSAGE TO THE CHANNEL USING THE CONTEXT OBJECT.
	await ctx.channel.send(ans)


@client.command(name='colour')
async def test(ctx): 
    retStr = str("""```diff\nHow's green ????```""") 
    await ctx.send(retStr)
@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member,*,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'The User {member} has been banned from the server')
@ban.error
async def ban_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("You do not have required permission for the action performed")






client.run('MTA0NDIwNDkwMDgxODYzMjc4NQ.GAOpKZ.bvJkJKiJeU8tO_0tMYMmt1-rX5q60YWgOWjGqo')


