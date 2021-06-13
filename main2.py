import discord
from discord.ext import commands
import json
import datetime
bot = commands.Bot(command_prefix="CC.",intents=discord.Intents.all())
config = {"white_list":[],"log_channel":None,"role_whitelist":[]}
def save():
	with open("save.json","w") as f:
		json.dump(config, f)



def load():
	with open("save.json","r") as f:
		config = json.load(f)

try:
	load()
except Exception as e:
	print(e,":","можно игнорить")
	save()
@commands.is_owner()
@bot.command()
async def set_log_channel(ctx,id:discord.TextChannel):
	config["log_channel"] = id.id
	await ctx.send("успешно установлено")
	save()
@commands.is_owner()
@bot.command()
async def add(ctx,user:discord.Member):
	config["white_list"].append(user.id)
	await ctx.send("успешно установлено")
	save()

@commands.is_owner()
@bot.command(name="del")
async def delete(ctx,user:discord.Member):
	try:
		config["white_list"].remove(user.id)
		await ctx.send("успешно удален")
		save()
	except:
		await ctx.send("такого юзера нет в списке")

@commands.is_owner()
@bot.command()
async def show(ctx):
	template = "```"
	for user in config["white_list"]:
		template = template + " " + bot.get_user(user).name
	template = template + "```"
	await ctx.send(template)
@commands.is_owner()
@bot.command()
async def clear(ctx):
	config["white_list"] = []
	await ctx.send("успешно очищено")
	save()

#роли



@commands.is_owner()
@bot.command()
async def add_role(ctx,role:discord.Role):
	config["role_whitelist"].append(role.id)
	await ctx.send("успешно установлено")
	save()

@commands.is_owner()
@bot.command()
async def del_role(ctx,role:discord.Role):
	try:
		config["role_whitelist"].remove(role.id)
		await ctx.send("успешно удалено")
		save()
	except:
		await ctx.send("такой роли нет в списке")

@commands.is_owner()
@bot.command()
async def show_role(ctx):
	template = "```"
	for role in config["role_whitelist"]:
		template = template + " " + ctx.guild.get_role(role).name
	template = template + "```"
	await ctx.send(template)
@commands.is_owner()
@bot.command()
async def clear_role(ctx):
	config["role_whitelist"] = []
	await ctx.send("успешно очищено")
	save()





def get_current_time() -> datetime:
        delta = datetime.timedelta(hours=3, minutes=0)
        return datetime.datetime.now(datetime.timezone.utc) + delta

@bot.event
async def  on_member_update(before, after):
	global config
	now = get_current_time()
	if before.status != after.status:
		if after.id in config["white_list"]:
			await bot.get_channel(config["log_channel"]).send(f"```{now} участник {after.name} сменил статус с {before.status} на {after.status} ```")
		else:
			for role in after.roles:
				if role.id in config["role_whitelist"]:
					await bot.get_channel(config["log_channel"]).send(f"``` {now} участник {after.name} сменил статус с {before.status} на {after.status} ```")
					break


import os
token = os.environ["TOKEN"]
bot.run(token)
