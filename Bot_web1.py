import discord
# client = discord.Client()
from discord.ext import commands

# intents : action qui se passe au niveau des utilisateurs. 
# Quand on créé notre client on va récupérer les intents par défault
# Il faut le définir = true : activer (mesure de protection donc il est demandé de l'activé)
# Le passer en paramètre lors de la demande client (discord.client(ici))

# Les mentions et les messages privés
# On peux envoyer un message privé à un user (voir dans le cours "$dm")
# On peux récupérer l'ensemble des mentions (ex: @nomdelapersonne) fait dans un message 
# Pour récup des infos on doit avoir le pseudo, la mention ne marche pas
# On doit découper le message pour extraire juste ce que je veux avec split(" ")

# Le client : il y a tt les infos du serveur dedans(ex: nb de personnes connecté, image du serveur, nom du serveur....)
# On peux aussi les récup via ctx 
#discord.embed : on peux insérer une carte avec couleur, nom, image avec embed.add_fields (voir le cours)

client = commands.Bot(command_prefix='$')

@client.command()
async def coucou(ctx):
    await ctx.send("COUCOU!!!")
# aller voir la doc de discord.py ex: FFmegOpusAudio pour traiter de la musique etc... 
# On a l'ensemble des events dans Event Reference dans le doc(ex: discord.on_typing quand qq'un est en train de taper)    
@client.command()
async def super_coucou(ctx,arg1,arg2):
 await ctx.send(arg1+" -- "+arg2)
 
# Faire le Bot

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    
    #Je copie l'identifiant de mon serveur par clique droit sur un salon (je dois être en mode développeur => voirn paramètres avancés de mon profil discord)
    Help_channel = client.get_channel(978578279374147614)
    
    #on met un symbole que l'on utilisera pas dans la discussion afin que le bot ne se déclenche pas si on dit 'help'
    if message.channel == Help_channel and message.content.startswith('$help'):
        await Help_channel.send('Bonjour!')
    if message.content == 'del':
        await message.channel.purge(limit=3)
        
    if message.content.startswith("$dm"): 
        user = message.mentions[0]
        strs = message.content.split(" ")
        await user.send(strs[2:])
    # Avec cette ligne on peux donc utiliser autant $help que !coucou car on demande de passer par tous le process de la fonction
    await client.process_commands(message)

@client.event
# Evenement lié aux intents donc marche que si on a bien initialiser les intents (voir au début du code)
async def on_member_join(member):
    Help_channel = client.get_channel(978578279374147614)
    await Help_channel.send('Bonjour' + member.display_name)

@client.command()
async def server(ctx):
    name = ctx.guild.name
    description = ctx.guild.description
    owner = ctx.guild.owner
    id = ctx.guild.id
    region = ctx.guild.region
    member_count = ctx.guild.member_count
    icon = ctx.guild.icon_url
# Pour avoir une carte stylisée dans discord avec des infos sur le serveur
    embed = discord.Embed(
        title = name ,
        description = description,
        color = discord.Color.red()
    )
    embed.set_thumbnail(url = icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server Id", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True) #deprecated
    embed.add_field(name="Member Count", value=member_count, inline=True)
    
    await ctx.send(embed = embed)

client.run("OTc4MjI4ODkwMDU1MDgyMDI1.GFF-JZ.sQKx8qynrWm8HkXZoEBL5mqzIwCb1CP-o4Bkz4")

# Projet à rendre jeudi prochain