import discord
from discord.ext import commands as discordCommands

from commands import grabar_clase, captura_de_pantalla


with open('token.txt') as f:
    token = f.read()
client = discordCommands.Bot(command_prefix = '!', intents = discord.Intents.all()) #Prefijo del bot


@client.command(name = 'grabar_clase')
async def cmd_grabar_clase(ctx, *args):
    await grabar_clase.exec(ctx, args)

@client.command(name = 'captura_de_pantalla')
async def cmd_captura_de_pantalla(ctx, *args):
    await captura_de_pantalla.exec(ctx, args)


client.run(token)