#Enju
import discord
import random
import time
import os
import asyncio
import pickle
import io
from discord.ext import commands
from discord.ext.commands import Bot


bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.event
async def on_ready():
	print ("Enju au rapport !")
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='!aide'))

@bot.check
async def botcheck(ctx):
    return not ctx.message.author.bot

@bot.command()
async def aide(ctx):
    em = discord.Embed(title="Commandes d'Enju", description="", color=discord.Colour.green())
    em.set_author(name="")
    em.add_field(name="!enju", value="Envoie une image d`Enju", inline=False)
    em.add_field(name="!avatar", value="Affiche l'avatar d'un utilisateur", inline=False)
    em.add_field(name="!emoji", value="Affiche un emoji en plus gros", inline=False)
    await ctx.send(embed=em)


@bot.command(pass_context=True)
async def purge(ctx, nombre):
	if ctx.author.id == 222017802087825408:
		await bot.purge_from(ctx.message.channel, limit=int(nombre))
	else :
		msg = await ctx.send("Seul mon Kinji peut utiliser cette commande !")
		await autoreaction(ctx, msg)

@bot.command(pass_context=True)
async def enju(ctx):
    fp = "Donnes/Img/Enju/{}".format(random.choice(os.listdir("Donnes/Img/Enju")))
    await ctx.send(file=discord.File(fp))

@bot.command(pass_context=True)
async def dit(ctx, *, message):
    if ctx.author.id == 222017802087825408:
        msg = await ctx.send(str(message))
        await autoreaction(ctx, msg)
    else:
        msg = await ctx.send("Seul mon Kinji peut utiliser cette commande !")
        await autoreaction(ctx, msg)



@bot.command(pass_context=True)
async def dits(ctx, *, message):
    if ctx.author.id == 222017802087825408:
        msg = await ctx.send(str(message))
        await ctx.message.delete()
        await autoreaction(ctx, msg)
    else:
        msg = await ctx.send("Seul mon Kinji peut utiliser cette commande !")
        await autoreaction(ctx, msg)


@bot.command(pass_context=True)
async def emoji(ctx, emoji: discord.Emoji):
    #embed = discord.Embed(title = ":{}:".format(emoji.name),color=0x4286f4)
    embed = discord.Embed(color=0x4286f4)
    embed.set_image(url=emoji.url)
    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
    embed = discord.Embed(title="Avatar de {}".format(user.name), color=0xff0000)
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)


async def autoreaction(ctx, msg):
    await msg.add_reaction(":enju:463080771465510912")
    await bot.wait_for("reaction_add", timeout=40, check=lambda r, u: u == ctx.author and r.message.id == msg.id)

bot.run(os.getenv("TOKEN"))
