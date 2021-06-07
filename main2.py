import discord
from discord.ext import commands
from json import dump,load
from os import environ
msg = ""
ignore_id = []
def save():
	global msg
	with open("save.cfg","w") as f:
		dump(msg,f)
def load():
	global msg
	with open("save.cfg") as f:
		msg = load(msg,f)
bot = commands.Bot(command_prefix="rass.",self_bot=True)

#a
@bot.event
async def on_message(message):
	global msg
	global load
	global ignore_id
	await bot.process_commands(message)
	try:
		load()
	except:
		pass
	if message.guild is None:
		if msg:
			if not message.author.id in ignore_id:
				if message.author.id != bot.client.id:
					await message.channel.send(msg)
					ignore_id.append(message.author.id)
@commands.is_owner()
@bot.command()
async def set_string(ctx,*,string):
	global msg
	global save
	msg = string
	await ctx.message.send("установлено")
	save()

bot.run(environ["TOKEN"],bot=False)
