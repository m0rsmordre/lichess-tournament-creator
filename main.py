import requests
import json
import random
import string

def random_n(N):
    return ''.join(random.choice(string.ascii_lowercase+ string.ascii_uppercase + string.digits) for _ in range(N))
def random_pass(N):
    return ''.join(random.choice(string.digits) for _ in range(N))

from discord_webhook import DiscordWebhook,DiscordEmbed

allowed_mentions = {"roles": ["841992808206565436"]}#Etiketlemek istediğiniz rolün idsi - ID of the role you want to mention
webhook = DiscordWebhook(url="WEBHOOK_URL",username="Chess Tournament", allowed_mentions=allowed_mentions,content="<@&841992808206565436>")




tournamet_link = "https://lichess.org/api/tournament"
token = "YOUR_LICHESS_TOKEN" #Needs OAuth2 - OAuth2 gerekiyor
headers = {"Authorization": "Bearer {}".format(token)}
waitMinutes = 60
password = random_pass(4)
tempo = 5
arti = 0
sure=60
description = "This tournament created by a bot.\nBu turnuva bot tarafından otomatik olarak oluşturuldu.\n Discord Server: discord.gg/ddcTr9sGE6"
turnuva_ismi = random_n(7) + " Arena"
rated = True

data = {
                "name": turnuva_ismi,
                "waitMinutes": waitMinutes,
                "password": password,
                "clockTime": tempo,
                "clockIncrement": arti,
                "minutes": sure,
                "description": description
        }
                
r = requests.post(tournamet_link, headers = headers,data=data)
print(r.content)

veri = r.json()


if(r.status_code < 300):
    embed = DiscordEmbed(title='{} is starting'.format(turnuva_ismi))
    #embed.add_embed_field(name='Turnuva İsmi', value=turnuva_ismi,inline=True)
    embed.add_embed_field(name='Starting in', value="{} minutes".format(waitMinutes) ,inline=True)
    embed.add_embed_field(name='Tempo', value="{}+{}".format(tempo,arti),inline=True)
    embed.add_embed_field(name='Duration', value="{} minutes".format(sure),inline=True)
    if(len(password) >0):
        embed.add_embed_field(name='Password', value=password,inline=True)
    
    if(rated):
        embed.add_embed_field(name='Is rated?', value="Yes",inline=True)
    else:
        embed.add_embed_field(name='Is rated?', value="No",inline=True)
    embed.add_embed_field(name="Tournament Link",value="[Click to join](https://lichess.org/tournament/{})".format(veri["id"]),inline=True)
    webhook.add_embed(embed)
    response = webhook.execute()

