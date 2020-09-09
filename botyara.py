import discord
#import dialogai
import apiai, json
import os
import commands as c
import requests
token = os.environ.get('TOKEN')
SDC_TOKEN = os.environ.get('SDC')
APIAI = os.environ.get("API")
def msg(s,id):
	request = apiai.ApiAI(APIAI).text_request()
	request.lang = 'ru'
	request.session_id = str(id)
	request.query = s 
	responseJson = json.loads(request.getresponse().read().decode('utf-8'))
	response=''
	Name = ''
	try:
		response = responseJson['result']['fulfillment']['speech']
	except:
		response = ""
	try:
		Name = responseJson['result']['metadata']['intentName']
	except:
		Name = ""
	#print(responseJson)
	msgk = [response,Name]
	if response != "":
		return msgk
	else:
		msgk[0] = "на данный момент я не могу понять что вы написали"
		return msgk
        
# поиск аргументов
class Myclient(discord.Client):
	async def on_ready(self):
		print('login {0}'.format(self.user))
		servers_count = len(super().guilds)
		head = {
		"Authorization":SDC_TOKEN
		}
		
		datas = {
		"servers":servers_count,
		"shards":1
		}
		dcs = requests.post("https://api.server-discord.com/v2/bots/724849666792882226/stats",headers=head,data=datas)
	async def on_message(self, message):
		try:
			ping1 = message.mentions[0]
		except:
			ping1 = None
		cmd = message.content
		message_args = c.FindArgs(cmd.replace("AI!", ""))
		if message_args != None:
			message_args[0]=message_args[0].replace("!W","")
			execute = message_args[0]
		else:
			execute = cmd.replace("AI!", "")
		if message.content[0:3] == "AI!" or message.content[0:2] == "W!":
			AImsg = msg(execute,message.author.id)
			if AImsg != None:
				if AImsg[1] == "my.ban":
					await c.CBan(message,message_args)
				elif AImsg[1] == "my.cat":
					await c.nya(message.channel)
				else:
					servers_count = len(super().guilds)
					head = {"Authorization":SDC_TOKEN}
					datas = {"servers":servers_count,"shards":1}
					dcs = requests.post("https://api.server-discord.com/v2/bots/724849666792882226/stats",headers=head,data=datas)
					await message.channel.send(AImsg[0])
		elif ping1 != None:
			if ping1.name == "Waifu-AI":
				tempArgs = message.content.split(" ",1)
				#print(tempArgs)
				AImsg = msg(tempArgs[1],message.author.id)
				await message.channel.send(AImsg[0])


hy = Myclient()
hy.run(token)