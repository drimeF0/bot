import discord
from PIL import Image,ImageDraw,ImageFont
from discord.ext import commands
bot = commands.Bot(command_prefix="bb.",intents=discord.Intents.all())
import asyncio
import io
import datetime


async def update_banner():
	global bot
	await bot.wait_until_ready()
	guild = bot.get_guild(740487178773200978)
	while True:
		img = Image.open("banner.jpg")
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype("20082.ttf",20)
		# draw.text((0, 0),"Sample Text",(255,255,255),font=font)
		print((
			int(img.size[0]/2), int(img.size[1]/2)
			 ))
		#time
		delta = datetime.timedelta(hours=3, minutes=0)
		tmp = datetime.datetime.now(datetime.timezone.utc) + delta
		now = tmp.strftime("%H:%M")
		draw.text((30,200),now,(255,255,255),font=font)
		#members (online)
		members_online = 0
		for member in guild.members:
			if member.status != discord.Status.offline:
				members_online += 1
		draw.text((350,250),f"{members_online} online",(255,255,255),font=font)
		#members
		draw.text((350,230),f"{guild.member_count} members",(255,255,255),font=font)
		#members in voices
		members_voice = 0
		for voice in guild.voice_channels:
			members_voice += len(voice.members)
		draw.text((30,250),f"{members_voice} in voice",(255,255,255),font=font)
		data = io.BytesIO()
		img.save(data,"PNG")
		data = data.getvalue()
		await guild.edit(banner=data)	
		await asyncio.sleep(10)

bot.loop.create_task(update_banner())
import os
token = os.environ['TOKEN']
bot.run(token)
