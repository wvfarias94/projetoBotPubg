import json
from typing import Text
import discord
from discord.ext import commands
from discord.ext.commands.core import command
from discord.flags import Intents
import random
import requests
from PIL import Image, ImageDraw, ImageFont, ImageOps
from io import BytesIO



with open('config.json') as e:
    infos = json.load(e)
    TOKEN = infos['token']
    prefixo = infos['prefix']

client =  commands.Bot(command_prefix=prefixo, Intents=discord.Intents.all())

########################################################################################################################################################################
#Gerando eventos 


#Bot dá boas vindas e apresenta uma imagem com o nome e o avatar do novo participante do server
@client.event
async def on_member_join(member):
    channel = client.get_channel("842058665532063795")

    url = requests.get(member.avatar_url)
    avatar = Image.open(BytesIO(url.content))
    avatar = avatar.resize((130, 130));
    bigsize = (avatar.size[0] * 3,  avatar.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(avatar.size, Image.ANTIALIAS)
    avatar.putalpha(mask)

    output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    output.save('avatar.png')

    #avatar = Image.open('avatar.png')
    fundo = Image.open('base.png')
    fonte = ImageFont.truetype('arial.ttf',70)
    escrever = ImageDraw.Draw(fundo)
    escrever.text(xy=(180,164), text=member.name,fill=(0,0,0),font=fonte)
    fundo.paste(avatar, (40, 90), avatar)
    fundo.save('bv.png')

    await client.send_file(channel, 'bv.png')

#imprimir no console  algumas informações na execução do bot a nivel de terminal
@client.event
async def on_ready():
    print(f'Bot online!\nID: {client.user.id})\nNome: {client.user}')

########################################################################################################################################################################
#gerando comandos para o bot


#comando status
@client.command()
async def status(ctx):
    await ctx.send('Olá, sou o Pega Flango!! Sou de autoria do Wagner Farias, \nfui desenvolvido no dia 12/05/2021 no intuito de ajudar a organizar o canal!!')

#comando moeda que randomiza cara ou coroa
@client.command(aliases=['cara', 'coroa', 'caraoucoroa'])
async def moeda(ctx):
    var = random.randint(1, 2)
    if var == 1: #Cara
        await ctx.send(' 😁 Cara ')
    elif var == 2: #Coroa   
        await ctx.send(' 👑 Coroa')
    
    ###############################################################################################################################################################################
#token do bot


client.run('ODQxMzYxNjIxMTQ1NzQ3NDU3.YJlpEg.cGf_ERlS-bpDyVHG5Fid0nCmYWc')


#teste para gitsa