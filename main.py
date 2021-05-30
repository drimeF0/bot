import discord
from discord.ext import commands
import json
from datetime import datetime
bot = commands.Bot(command_prefix="CC.",intents=discord.Intents.all())
log_channel = None
try:
	log_channel = open("channel_log").read()
	log_channel = int(log_channel)
except Exception as e:
	print(e)
	print(type(e))
@bot.command()
async def set_log_channel(ctx,id:discord.TextChannel):
	global log_channel
	log_channel = id.id
	f = open("channel_log","w")
	f.write(str(log_channel))
	f.close()
	await ctx.send("успешно установлено")
@bot.event
async def  on_member_update(before, after):
	global log_channel
	global white_list
	now = datetime.now()
	if before.status != after.status:
		await bot.get_channel(log_channel).send(f"{now} участник {after.name} сменил статус с {before.status} на {after.status}")



bot.run("токен-бота")
