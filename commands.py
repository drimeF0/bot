def FindArgs(text):
	e = 0
	a = False
	for e in range(len(text)):
		if text[e] == "-":
			Args = text.split("-")
			a = True
			break
		else:
			e = e + 1
	if a == True:
		return Args
	else:
		return None

import discord
#import Parser as ps
async def CBan(message, message_args):
	member = message.mentions
	author = discord.utils.get(message.guild.members, name=message.author.name)
	if author.permissions_in(message.channel).ban_members == True:
		try:
			membar = member[0].name
		except:
			await message.channel.send("укажите в первом аргументе пинг юзера")
		try:
			baned = discord.utils.get(message.guild.members, name=membar)
		except:
			await message.channel.send("юзер не найден!")
		try:
			await baned.ban(reason=message_args[2])
			await message.channel.send(" юзер " + membar + " забанен по причине " + message_args[2])
		except:
			await message.channel.send("не удалось забанить")
	else:
		await message.channel.send(author.mention + " вы не можете банить участников")
		
async def Ckick(message,message_args):
	author = discord.utils.get(message.guild.members, name=message.author.name)
	User = message.mentions
	try:
		userName = User[0].name
	except:
		await message.channel.send("укажите юзера через пинг")
		return
	kickUser = discord.utils.get(message.guild.members, name=userName)
	if author.permissions_in(message.channel).kick_members == True:
		try:
			await KickUser.kick(reason=message_args[2])
		except:
			await message.channel.send("не удалось кикнуть")
			return
	else:
		await message.channel.send(author.mention + " вы не можете кикать участников")


async def nya(channel):
	await channel.send("""
░░▓▓░░░░░░░░▓▓░░
░▓▒▒▓░░░░░░▓▒▒▓░
░▓▒▒▒▓░░░░▓▒▒▒▓░
░▓▒▒▒▒▓▓▓▓▒▒▒▒▓░
░▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓
▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓
▓▒▒▒░▓▒▒▒▒▒░▓▒▒▓
▓▒▒▒▓▓▒▒▒▓▒▓▓▒▒▓
▓▒░░▒▒▒▒▒▒▒▒▒░░▓
▓▒░░▒▓▒▒▓▒▒▓▒░░▓
░▓▒▒▒▓▓▓▓▓▓▓▒▒▓░
░░▓▒▒▒▒▒▒▒▒▒▒▓░░
░░░▓▓▓▓▓▓▓▓▓▓░░░""")


async def clear(message,args):
	author = discord.utils.get(message.guild.members, name=message.author.name)
	if author.permissions_in(message.channel).manage_messages == True:
			message.channel.delete_messages(int(args[1]))