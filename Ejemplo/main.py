import os
import discord
from discord.ext import commands


token = open('token.txt').read()
bot = commands.Bot(command_prefix = '!', intents = discord.Intents.all()) #Prefijo del bot


@bot.command(name = 'suma') #Funcion que realizara la suma entre dos numeros enteros
async def sumar(ctx, num1, num2):
    response = int(num1) + int(num2)
    await ctx.send(response)

@bot.command(name = 'exec') #Funcion que realizara la suma entre dos numeros enteros
async def multiplicar(ctx, command):
    print(command)
    await ctx.send(command)

@bot.command(name = 'grabar_clase') #Funcion que realizara la suma entre dos numeros enteros
async def multiplicar(ctx):
    await ctx.send('Por desarrollar')

@bot.command(name = 'captura_de_pantalla') #Funcion que realizara la suma entre dos numeros enteros
async def multiplicar(ctx, *args):
    print(args)
    await ctx.send('Por desarrollar')

bot.run(token)