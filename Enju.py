#Enju
import discord
import random
import time
import os
import aiohttp
import requests
import asyncio
import pickle
import random
import io
from discord.ext import commands
from discord.ext.commands import Bot
from discord import opus
import discord
from discord.ext import commands
import youtube_dl
import ffmpeg


def get_metadata(query):
    return youtube_dl.YoutubeDL({
        "format": "ogg[abr>0]/m4a[abr>0]/webm[abr>0]/bestaudio/best",
        "ignoreerrors": True,
        "default_search": "auto",
        "source_address": "0.0.0.0",
        "quiet": True
    }).extract_info(query, download=False)['url']



OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']

def load_opus_lib(opus_libs=OPUS_LIBS):

    if opus.is_loaded():

        return True

    for opus_lib in opus_libs:

        try:

            opus.load_opus(opus_lib)

            return

        except OSError:

            pass

    raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))

#load_opus_lib()

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')
players = {}
opts = {}




@bot.event
async def on_ready():
	print ("Enju au rapport !")
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='!aide'))

@bot.check
async def botcheck(ctx):
    return not ctx.message.author.bot

@bot.command()
async def aide(ctx):
    em = discord.Embed(title="Commandes d'Enju", description="", color=discord.Colour.orange())
    em.set_author(name="")
    em.add_field(name="!enju", value="Envoie une image d'Enju", inline=False)
    em.add_field(name="!avatar", value="Affiche l'avatar d'un utilisateur", inline=False)
    em.add_field(name="!emoji", value="Affiche un emoji custom du serveur en plus gros", inline=False)
    em.add_field(name="!jtm", value="Déclare ta flamme à Enju", inline=False)
    em.add_field(name="!dommage", value="Ah c'est dommage", inline=False)
    em.add_field(name="!neko", value="Envoie une image de neko", inline=False)
    em.add_field(name="!loli", value="Envoie une image de loli", inline=False)
    em.add_field(name="!lewdneko", value="Envoie une image érotique de neko", inline=False)
    em.add_field(name="!hentai", value="Envoie une image de hentai", inline=False)
    em.add_field(name="!join", value="Fait rejoindre Enju dans le channel vocal actuel", inline=False)
    em.add_field(name="!parle", value="Fait jouer un extrait aléatoire d'Enju dans ce channel vocal", inline=False)
    em.add_field(name="!play", value="Joue une musique depuis un lien youtube dans ce channel vocal", inline=False)
    em.add_field(name="!pause", value="Met la musique qui est jouée en pause", inline=False)
    em.add_field(name="!resume", value="Reprend la musique si elle est en pause", inline=False)
    em.add_field(name="!stop", value="Arrête la musique qui est actuellement jouée", inline=False)
    em.add_field(name="!leave", value="Fait quitter Enju du channel vocal dans lequel elle se trouve", inline=False)
    em.add_field(name="___________________________________________", value="Bot codé par Kinji", inline=False)


    em.set_thumbnail(url = "https://i.gyazo.com/4f452d2b77748f7561902cc0fe824d37.png")
    await ctx.send(embed=em)


@bot.event
async def on_member_join(member):
    await member.send('Bienvenue dans la Tanière des weebs !! Si jamais tu souhaites avoir ton petit nom, il te suffit du Nom et de la Couleur dans le channel #demande-de-role ! Sur ce, je te souhaite une bonne compagnie dans cette tanière ! Une dernière chose, cette tanière possède son propre bot codé par Kinji ! Si jamais tu veux voir ses commandes utilise !aide ! 😉')
    role = discord.utils.get(member.guild.roles, name="Membres")
    await member.add_roles(role)



@bot.command()
async def purge(ctx, amount):
	if ctx.author.id == 222017802087825408:
		await ctx.channel.purge(limit=int(amount))
	elif ctx.author.id == 363059393601994752:
		await ctx.channel.purge(limit=int(amount)) 
	elif ctx.author.id == 339157038384939008:
		await ctx.channel.purge(limit=int(amount))
	elif ctx.author.id == 259424383628607493:
		await ctx.channel.purge(limit=int(amount))
	elif ctx.author.id == 298209441185005578:
		await ctx.channel.purge(limit=int(amount))
	else :
		msg = await ctx.send("Seul mon Kinji (et ses admins) peuvent utiliser cette commande !")
		await autoreaction(ctx, msg)

@bot.command()
async def dommage(ctx):
    await ctx.channel.purge(limit=int(1))
    msg = await ctx.send("https://www.youtube.com/watch?v=8AF-Sm8d8yk")
    await msg.add_reaction(":enju:463080771465510912")


@bot.command()
async def parle(ctx):
	channel = ctx.message.author.voice.channel
	fp = "Data/Audio/Enju/{}".format(random.choice(os.listdir("Data/Audio/Enju")))
	ctx.voice_client.play(discord.FFmpegPCMAudio(fp), after=None)

@bot.command()
async def enju(ctx):
    fp = "Data/Img/Enju/{}".format(random.choice(os.listdir("Data/Img/Enju")))
    await ctx.send(file=discord.File(fp))


@bot.command()
async def batman(ctx):
    fp = "Data/Img/Batman/{}".format(random.choice(os.listdir("Data/Img/Batman")))
    await ctx.send(file=discord.File(fp))

@bot.command()
async def redhood(ctx):
    fp = "Data/Img/RedHood/{}".format(random.choice(os.listdir("Data/Img/RedHood")))
    await ctx.send(file=discord.File(fp))

@bot.command()
async def flash(ctx):
    fp = "Data/Img/Flash/{}".format(random.choice(os.listdir("Data/Img/Flash")))
    await ctx.send(file=discord.File(fp))


@bot.command()
async def loli(ctx):
    fp = "Data/Img/Loli/{}".format(random.choice(os.listdir("Data/Img/Loli")))
    await ctx.send(file=discord.File(fp))


@bot.command()
async def jtm(ctx):
    if ctx.author.id == 222017802087825408:
        msg = await ctx.send("Moi aussi !! ❤")
        await msg.add_reaction(":enju:463080771465510912")
        await msg.add_reaction("❤")
    else:
        msg = await ctx.send("Mon coeur appartient à Kinji")
        await msg.add_reaction(":enju:463080771465510912")
        await msg.add_reaction("💔")



@bot.command()
async def neko(ctx):
	async with aiohttp.ClientSession() as cs:
		async with cs.get('https://nekos.life/api/v2/img/neko') as res:

			js = await res.json()
			embed = discord.Embed(colour=discord.Colour.orange())
			embed.set_image(url=js['url'])
			await ctx.send(embed=embed)


@bot.command()
async def lewdneko(ctx):

	if ctx.message.channel.is_nsfw() is False:
   		 await ctx.send("🔞 Pas de choses obscènes dans ce channel ! 🔞")
	if ctx.message.channel.is_nsfw() is True:
		async with aiohttp.ClientSession() as cs:
			async with cs.get('https://nekos.life/api/lewd/neko') as res:
				js = await res.json()
				await ctx.channel.purge(limit=int(1))
				embed = discord.Embed(colour=discord.Colour.orange())
				embed.set_image(url=js['url'])
				await ctx.send(embed=embed)


@bot.command()
async def hentai(ctx):

	if ctx.message.channel.is_nsfw() is False:
   		 await ctx.send("🔞 Pas de choses obscènes dans ce channel ! 🔞")
	if ctx.message.channel.is_nsfw() is True:
		async with aiohttp.ClientSession() as cs:
			async with cs.get('https://nekos.life/api/v2/img/hentai') as res:
				js = await res.json()
				await ctx.channel.purge(limit=int(1))
				embed = discord.Embed(colour=discord.Colour.orange())
				embed.set_image(url=js['url'])
				await ctx.send(embed=embed)


@bot.command()
async def dit(ctx, *, message):
    if ctx.author.id == 222017802087825408:
        msg = await ctx.send(str(message))
        await ctx.message.delete()
        await autoreaction(ctx, msg)
    else:
        msg = await ctx.send("Seul mon Kinji peut utiliser cette commande !")
        await autoreaction(ctx, msg)



@bot.command()
async def emoji(ctx, emoji: discord.Emoji):
    embed = discord.Embed(color=0xE8A200)
    embed.set_image(url=emoji.url)
    await ctx.send(embed=embed)


@bot.command()
async def avatar(ctx, user: discord.Member):
    embed = discord.Embed(title="Avatar de {}".format(user.name), color=0xE8A200)
    embed.set_image(url=user.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def join(ctx):
	channel = ctx.message.author.voice.channel
	await channel.connect()
	msg = await ctx.send('💫 Me voilà !💫')
	await msg.add_reaction(":enju:463080771465510912")

@bot.command()
async def leave(ctx):
	await ctx.voice_client.disconnect()
	msg = await ctx.send('💨 Bye !💨')
	await msg.add_reaction(":enju:463080771465510912")


@bot.command()
async def play(ctx, url):

	url = await ctx.bot.loop.run_in_executor(None, get_metadata, url)
	msg = await ctx.send('🏁Et voilà !🏁')
	await msg.add_reaction(":enju:463080771465510912")


	ffmpeg = discord.FFmpegPCMAudio(url)


	ctx.voice_client.play(ffmpeg)

@bot.command()
async def pause(ctx):
	ctx.voice_client.pause()
	msg = await ctx.send('⛔ Vidéo mise en pause ! ⛔')
	await msg.add_reaction(":enju:463080771465510912")

@bot.command()
async def resume(ctx):
	ctx.voice_client.resume()
	msg = await ctx.send('🎶 Reprise de la vidéo ! 🎶')
	await msg.add_reaction(":enju:463080771465510912")

@bot.command()
async def stop(ctx):
	ctx.voice_client.stop()
	msg = await ctx.send('❌ Vidéo arrêtée ! ❌')
	await msg.add_reaction(":enju:463080771465510912")


async def autoreaction(ctx, msg):
    await msg.add_reaction(":enju:463080771465510912")


bot.run(os.getenv("TOKEN"))
