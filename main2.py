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
	try:
		load()
	except:
		pass
	if message.guild is None:
		if not message.author.bot:
			if msg:
				if not message.author.id in ignore_id:
					await message.channel.send(msg)
					ignore_id.append(message.author.id)
		await bot.process_commands(message)
@commands.is_owner()
@bot.command()
async def set_string(ctx,*,string):
	global msg
	global save
	msg = string
	await ctx.send("установлено")
	save()

bot.run(environ["TOKEN"],bot=False)
