import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

botsito=commands.Bot(command_prefix="/", intents=intents)

@botsito.event
async def on_ready():
    print(f"se inicio el bot {botsito.user}")

@botsito.command()
async def hola(ctx):
    await ctx.send("Hola, como estas")

@botsito.command()
async def suma(ctx,num1:int,num2:int):
    suma=num1+num2
    await ctx.send(f"el resultado de {num1} + {num2} = {suma}")

@botsito.command()
async def randomN(ctx,longitud: int):
    if longitud < 0:
        await ctx.send("La longitud de tu numero no puede ser menor a 0")
        return
        
    numero_al_azar = random.randint(10**(longitud - 1), 10**longitud - 1)
    await ctx.send(f"Tu número aleatorio de {longitud} dígitos es: {numero_al_azar}")

@botsito.command()
async def resta(ctx,num1:int,num2:int):
    resta=num1-num2
    await ctx.send(f"el resultado de {num1} - {num2} = {resta}")

@botsito.command()
async def multiplica(ctx,num1:int,num2:int):
    multiplica=num1*num2
    await ctx.send(f"el resultado de {num1} * {num2} = {multiplica}")

@botsito.command()
async def divide(ctx,num1:int,num2:int):
    divide=num1/num2
    await ctx.send(f"el resultado de {num1} / {num2} = {divide}")



botsito.run("token")
