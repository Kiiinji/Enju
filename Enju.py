#Enju
import discord
import random
import time
import os 
import requests
import asyncio
import pickle
import random
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
    em.add_field(name="!enju", value="Envoie une image d'Enju", inline=False)
    em.add_field(name="!avatar", value="Affiche l'avatar d'un utilisateur", inline=False)
    em.add_field(name="!emoji", value="Affiche un emoji en plus gros", inline=False)
    em.add_field(name="!jtm", value="Déclare ta flamme à Enju", inline=False)
    em.add_field(name="!neko", value="Envoie une image de neko", inline=False)
    em.add_field(name="!loli", value="Envoie une image de loli", inline=False)
    em.add_field(name="!lewdneko", value="Envoie une image érotique de neko", inline=False)
    em.add_field(name="!hloli", value="Envoie une image H de loli", inline=False)
    em.add_field(name="!hentai", value="Envoie une image de hentai", inline=False)
    em.set_thumbnail(url = "https://i.gyazo.com/4f452d2b77748f7561902cc0fe824d37.png")
    await ctx.send(embed=em)


@bot.command(pass_context=True)
async def purge(ctx, amount):
	if ctx.author.id == 222017802087825408:
		await ctx.channel.purge(limit=int(amount))

	else :
		msg = await ctx.send("Seul mon Kinji peut utiliser cette commande !")
		await autoreaction(ctx, msg)



@bot.command(pass_context=True)
async def enju(ctx):
    fp = "Data/Img/Enju/{}".format(random.choice(os.listdir("Data/Img/Enju")))
    await ctx.send(file=discord.File(fp))


@bot.command(pass_context=True)
async def loli(ctx):
    fp = "Data/Img/Loli/{}".format(random.choice(os.listdir("Data/Img/Loli")))
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
async def jtm(ctx):
    if ctx.author.id == 222017802087825408:
        msg = await ctx.send("Moi aussi !! ❤")
        await msg.add_reaction(":enju:463080771465510912")
        await msg.add_reaction("❤")
    else:
        msg = await ctx.send("Mon coeur appartient à Kinji")
        await msg.add_reaction(":enju:463080771465510912")
        await msg.add_reaction("💔")




@bot.command(pass_context=True)
async def neko(ctx):
	r = requests.get('https://nekos.life/api/v2/img/neko')
	js = r.json()
	await ctx.send(js['url'])

@bot.command(pass_context=True)
async def lewdneko(ctx):
	if ctx.message.channel.is_nsfw() is False:
   		 await ctx.send("🔞 Pas de choses obscènes dans ce channel ! 🔞")
	if ctx.message.channel.is_nsfw() is True:
    		r = requests.get('https://nekos.life/api/v2/img/lewd')
	js = r.json()
	await ctx.channel.purge(limit=int(1))
	await ctx.send(js['url'])


@bot.command(pass_context=True)
async def hloli(ctx):
	if ctx.message.channel.is_nsfw() is False:
   		 await ctx.send("🔞 Pas de choses obscènes dans ce channel ! 🔞")
	if ctx.message.channel.is_nsfw() is True:
    		r = requests.get('https://nekos.life/api/v2/img/smallboobs')
	js = r.json()
	await ctx.channel.purge(limit=int(1))
	await ctx.send(js['url'])

@bot.command(pass_context=True)
async def hentai(ctx):
	if ctx.message.channel.is_nsfw() is False:
   		 await ctx.send("🔞 Pas de choses obscènes dans ce channel ! 🔞")
	if ctx.message.channel.is_nsfw() is True:
    		r = requests.get('https://nekos.life/api/v2/img/hentai')
	js = r.json()
	await ctx.channel.purge(limit=int(1))
	await ctx.send(js['url'])
	


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




bot.run(os.getenv("TOKEN"))



