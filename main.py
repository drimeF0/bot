import discord
from discord.ext import commands
import datetime
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
def get_current_time() -> datetime:
	delta = datetime.timedelta(hours=3, minutes=0)
	return datetime.datetime.now(datetime.timezone.utc) + delta
@bot.event
async def  on_member_update(before, after):
	global log_channel
	global white_list
	global get_current_time
	now = get_current_time()
	now = now.strftime("%m/%d/%Y, %H:%M:%S")
	if before.status != after.status:
		await bot.get_channel(log_channel).send(f"```{now} участник {after.name} сменил статус с {before.status} на {after.status}```")

bot.run(os.environ['TOKEN'])
