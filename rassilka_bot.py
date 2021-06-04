import discord
from discord.ext import commands
from json import dump,load
from os import environ
msg = ""
async def save():
	global msg
	with open("save.cfg","w") as f:
		dump(msg,f)
def load():
	global msg
	with open("save.cfg") as f:
		msg = load(msg,f)
bot = commands.Bot(command_prefix="rass.")


@bot.event
async def on_message(message):
	global msg
	global load
	load()
	if message.guild is None:
		await message.channel.send(msg)
	await bot.process_commands(message)
@bot.command()
@commands.is_owner()
async def set_string(ctx,*,string):
	global msg
	msg = string
	await ctx.send("установлено")

bot.run(environ["TOKEN"])