from ast import Try
import discord
import re
client = discord.Client()
from tree import *
from discord.ext import commands
client = commands.Bot(command_prefix="")

default_intents = discord.Intents.default()
default_intents.members = True
member = discord.Client(intents = default_intents)

#     embed.set_author(name=ctx.author.display_name, url="https://twitter.com/RealDrewData", icon_url=ctx.author.avatar_url)


@client.event
async def on_ready():
        print("Le bot est prêt.")

#lorsqu'on a un nouveau membre
@member.event
async def on_member_join(member):
    Help_channel = client.get_channel(978575214923350030)
    await Help_channel.send('Serenus vous souhaite la bienvenue !' + member.display_name)
    await Help_channel.send('Si vous voulez de l aide tapez : help' + member.display_name)
    await Help_channel.send('Si au cours de la  conversation vous voulez retourner en arriere tapez : back' + member.display_name)


# fonction quand l'utilisateur veut supprimer un message
@client.event
async def on_message(message):
    message.content = message.content.lower()

    if message.author == client.user:
        return

    if message.content == "del":
        await message.channel.purge(limit=3)

    await client.process_commands(message)
    


@client.command()
async def serenus(ctx,arg):
    if arg != "back":
        for child in current_path[-1].list_child_node:
            if child.keyword in arg:
                current_path.append(child)
                await ctx.channel.send(child.question)
        if current_path[-1].keyword not in arg:
            await ctx.send("! Mettez dans votre requête un des mots clés émis")
            await ctx.channel.send(current_path[-1].question)
                
    else:
        current_path.pop()
        await ctx.channel.send(current_path[-1].question)


@client.command()
async def stress(ctx):
    name = ctx.guild.name
    description = "ctx.guild.description"
    owner = ctx.guild.owner
    id = ctx.guild.id
    region = ctx.guild.region
    member_count = ctx.guild.member_count
    avatar = ctx.guild.icon_url

    embed = discord.Embed(
        title = name ,
        description = description,
        color = discord.Color.red()
    )
    embed.set_thumbnail(url = avatar)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server Id", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=member_count, inline=True)
    embed.set_thumbnail(url = "https://images.pexels.com/photos/1114690/pexels-photo-1114690.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2")
    embed.set_image(url = "https://images.pexels.com/photos/1408221/pexels-photo-1408221.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2")

    
    await ctx.send(embed = embed)
       
       
@client.command()
async def psychologue(ctx):
    name = "Rechercher un psychologue"
    description = "Psychologue, nous sommes à votre écoute.\
    Serenus vous invite à cliquer sur le titre ci-dessus pour accéder depuis partout en France à un psychologue."
     
    url = "https://www.doctolib.fr/psychologue"
    

    embed = discord.Embed(
        title = name,
        url = url,
        description = description,
        color = discord.Color.green()
    )
    
    embed.set_thumbnail(url = "https://images.pexels.com/photos/36717/amazing-animal-beautiful-beautifull.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
    embed.set_image(url = "https://images.pexels.com/photos/4098288/pexels-photo-4098288.jpeg")
    embed.set_footer(text="Auteur: {}".format(ctx.author.display_name))
    await ctx.send(embed = embed)


@client.command()
async def nathuropathe(ctx):
    name = "Rechercher un nathuropathe"
    description = "Psychanalystes, nous sommes là pour vous.\
    Serenus vous invite à cliquer sur le titre ci-dessus pour accéder depuis partout en France à un naturopathe."
     
    url = "https://www.doctolib.fr/naturopathe/france"
    author = "Amaury"

    embed = discord.Embed(
        title = name,
        url = url,
        description = description,
        color = discord.Color.orange()
    )
    
    embed.set_thumbnail(url = "https://images.pexels.com/photos/163186/globuli-medical-bless-you-homeopathy-163186.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
    embed.set_image(url = "https://images.pexels.com/photos/7772010/pexels-photo-7772010.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
    embed.set_footer(text="Auteur: {}".format(author))
    await ctx.send(embed = embed)
    
@client.command()
async def magnétiseur(ctx):
    name = "Rechercher un magnétiseur"
    description = "Psychanalystes, nous sommes là pour vous.\
    Serenus vous invite à cliquer sur le titre ci-dessus pour accéder depuis partout en France à un magnétiseur."
     
    url = "https://www.annuaire-magnetiseur.fr/"
    author = "Amaury"

    embed = discord.Embed(
        title = name,
        url = url,
        description = description,
        color = discord.Color.orange()
    )
    
    embed.set_thumbnail(url = "https://images.pexels.com/photos/4120840/pexels-photo-4120840.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
    embed.set_image(url = "https://images.pexels.com/photos/5240700/pexels-photo-5240700.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
    embed.set_footer(text="Auteur: {}".format(author))
    await ctx.send(embed = embed)

@client.command()
async def psychanaliste(ctx):
    name = "Rechercher un psychanalyste"
    description = "Psychanalystes, nous sommes là pour vous.\
    Serenus vous invite à cliquer sur le titre ci-dessus pour accéder depuis partout en France à un psychanalyste."
     
    url = "https://www.doctolib.fr/psychanalyste/france"
    author = "Amaury"

    embed = discord.Embed(
        title = name,
        url = url,
        description = description,
        color = discord.Color.orange()
    )
    
    embed.set_thumbnail(url = "https://images.pexels.com/photos/2775196/pexels-photo-2775196.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
    embed.set_image(url = "https://images.pexels.com/photos/5699465/pexels-photo-5699465.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
    embed.set_footer(text="Auteur: {}".format(author))
    await ctx.send(embed = embed)
    

@client.command()
async def psychiatre(ctx):
    name = "Rechercher un psychiatre"
    description = "Psychiatres, nous sommes là pour vous.\
    Serenus vous invite à cliquer sur le titre ci-dessus pour accéder depuis partout en France à un psychiatre."
     
    url = "https://www.doctolib.fr/psychiatre/france"
    author = "Amaury"

    embed = discord.Embed(
        title = name,
        url = url,
        description = description,
        color = discord.Color.orange()
    )
    
    embed.set_thumbnail(url = "https://images.pexels.com/photos/2662116/pexels-photo-2662116.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
    embed.set_image(url = "https://images.pexels.com/photos/4101137/pexels-photo-4101137.jpeg?cs=srgb&dl=pexels-cottonbro-4101137.jpg&fm=jpg")
    embed.set_footer(text="Auteur: {}".format(author))
    await ctx.send(embed = embed)
       
@client.command()
async def nutritionniste(ctx):
    name = "Rechercher un nutritionniste"
    description = "Nutritionnistes, nous sommes prêt à vous aider.\
    Serenus vous invite à cliquer sur le titre ci-dessus pour accéder depuis partout en France à un nutritionniste."
     
    url = "https://www.doctolib.fr/nutritionniste/france"
    author = "Amaury"

    embed = discord.Embed(
        title = name,
        url = url,
        description = description,
        color = discord.Color.orange()
    )
    
    embed.set_thumbnail(url = "https://images.pexels.com/photos/1128678/pexels-photo-1128678.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
    embed.set_image(url = "https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
    embed.set_footer(text="Auteur: {}".format(author))
    await ctx.send(embed = embed)
            

@client.command()
async def panic(ctx):
    name = ctx.guild.name
    description = "Voici une vidéo pour affronter une attaque de panique: cliquez sur Serenus."
     
 
    url = "https://www.youtube.com/watch?v=3nyQpBu2BSc"
    author = "Amaury"

    embed = discord.Embed(
        title = name,
        url = url,
        description = description,
        color = discord.Color.green()
    )
    
    embed.set_thumbnail(url = "https://images.pexels.com/photos/515631/pexels-photo-515631.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
    embed.set_image(url = "https://images.pexels.com/photos/355863/pexels-photo-355863.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
    embed.set_footer(text="Auteur: {}".format(author))
    await ctx.send(embed = embed)




@client.command()
async def dance(ctx):
    name = ctx.guild.name
    description = "Voici des vidéos pour les passionnés, les amoureux de danse et qui à travers cette pratique cherche l'évasion, \
        l'expression non verbale, la sensation de liberté, de légèreté et se vider l'esprit par le mouvement du corps"

    url = "https://youtu.be/PturM3jNZoQ" 
  
    author = "Nachmia"

    embed = discord.Embed(
        title = name,
        url = url,
        description = description,
        color = discord.Color.purple()
    )

    embed.set_thumbnail(url = "https://i.pinimg.com/originals/1b/e4/b2/1be4b2a8638a9b57e45fe8b518bb3c46.jpg%22") 
    embed.set_image(url = "https://www.superprof.fr/images/annonces/professeur-home-cours-salsa-bachata-kizomba-choregraphie-ouverture-bal-mariage.jpg%22")
    embed.set_footer(text="Auteur: {}".format(author))
    
    await ctx.send(embed = embed)


#quiz serenus

@client.command()
async def objectif(ctx):
    await ctx.send("Souvent, lorsque nous allons mal, nous formulons mal nos objectifs sans s'en rendre compte c'est à dire mentalement.")
    await ctx.send("Je vous propose ici de formuler consciement vos objectifs pour les rendre plus engageant c'est à dire que votre cerveau les écoutera plus et s'ensuivra l'action.")
    await ctx.send("Je vous présente donc trois objectifs, vous me dîtes en retour celui qui vous semble le mieux formulé. En retour, je vous donnerai de l'information pour améliorer les formulations.")
    await ctx.send("En retour, je vous donnerai de l'information pour améliorer les formulations.")
    await ctx.send("Voulez-vous jouer à ce jeu ? oui / non\n")


    def user_message(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel
    
    try:
        answer = await client.wait_for("message", timeout = 10, check = user_message)
    except:
        await ctx.send("Game over\nNous avons reçu aucune réponse de votre part !")
        return
    
    message = await ctx.send("\nVoici les 3 objectifs, répondez en cochant un des chiffres mentionnés:\n\n1️⃣Aller à la plage cet aprés-midi pour réduire mon anxiété\n\n2️⃣Réduire mon anxiété en pratiquant un exercice tous les matin à 7h avant de partir\n\n3️⃣Réduire mon anxiété en utilisant l'exercice de pranayama, la respiration inversée. Mon anxiété sera réduite si je me sens bien dans mon corps.\n")
    await message.add_reaction("1️⃣")
    await message.add_reaction("2️⃣")
    await message.add_reaction("3️⃣")

    def check_reaction(reaction, user):
        return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "1️⃣" or str(reaction.emoji == "2️⃣") or str(reaction.emoji == "3️⃣"))
    
    try:
        reaction, user = await client.wait_for("reaction_add", timeout = 10, check = check_reaction)
        if reaction.emoji == "1️⃣":
            await ctx.send("\n\nCe but n'est pas assez spécifique car nous ne savons pas quelle est la plage, ni l'heure précise d'engagement. \
                    \nIl lui manque aussi des informations sur l'action précise pour réduire votre anxiété. \
                    \nAssurez-vous aussi qu'il est réaliste: \nvous pouvez vous déplacer à la plage et rien de vous y empêche (travail etc...)\
                    \n\nAjoutez donc une heure ou une plage horaire: \nimaginer aussi en détail la scène de détente et engagez-vous par écrit à la réaliser.\
                    \nTrouver enfin un indicateur de satisfaction pour mesurer la baisse de votre anxiété aprés la plage.\n")

        elif reaction.emoji == "2️⃣":
            await ctx.send("\n\nCe but facilite l'engagement car il indique un rythme à un moment précis.\
                    \nIl lui manque en revanche de la spécificité car votre cerveau a besoin de se représenter en image précisément ce que vous allez faire.\
                    \nCette condition est importante pour se donner une réelle motivation à agir. \n\nAussi, comment savez-vous que votre anxiété a baissé ? Trouver un indicateur de satisfaction.\n")

        elif reaction.emoji == "3️⃣":
            await ctx.send("\n\n La formulation ici permet au cerveau de bien se représenter la méthode utilisée pour atteindre l'objectif et il est réaliste. Il y a aussi un critère de satisfaction.\
                    \nCette formulation gagnerait à s'améliorer si vous ajoutez par exemple une horaire, un rythme ou un évènement pour vous engagez à pratiquer à ce moment.\
                    \n\nLe critère de satisfaction peut être améliorer pour mieux visualiser ce qui se passe dans le corps si l'objectif est atteint.\n")

    except:
        await ctx.send("Fin de la partie ! Veuillez recommencer")

    
    
    
@client.command()
async def game_dialogue(ctx):
    await ctx.send("Bienvenue dans le jeu des rôles: apprenez à mieux résoudre un conflit au travers d'une histoire fictive.")
    await ctx.send("Vous serez mieux armé quand vous rencontrerez une situation similaire.")
    await ctx.send("Je vous présente un conflit potentiel et 3 réponses possibles, vous me dîtes en retour celle qui vous semble la plus à même de résoudre le conflit")
    await ctx.send("Voulez-vous jouer à ce jeu ? oui / non\n")


    def user_message(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel
    
    try:
        answer = await client.wait_for("message", timeout = 10, check = user_message)
    except:
        await ctx.send("Game over\nNous avons reçu aucune réponse de votre part !")
        return
    
    message = await ctx.send("\n Avant de connaître lire les réponses: \nfermer les yeux et prenez la place de la soeur de Delphine, imaginez bien tous les détails et sentiments par empathie. \n Puis choississez la réponse ci-dessous la plus appropriée selon vous:\
                            1️⃣\n\nVous allez voir vos parents pour leur dire: J'estime avoir le droit de prendre la voiture car ma soeur vient de la prendre et vous lui payez le permis en échange !\
                            2️⃣\n\nVous allez voir vos parents pour leur dire:\nEn payant des cours à Delphine vous entrez dans une spirale, elle risque de faire d'autres conneries par la suite.Je crois au contraire qu'il faudrait être ferme mais juste.\
                            3️⃣\n\n Vous allez directement voir votre soeur pour lui dire avec un ton ferme: \
                                \nTu as pris la voiture, sache que si tu recommence et que je suis la seule à le voir, je ne peux garder cela pour moi. \
                                \nJe serais bien obligé de le dire aux parents car cela mettra des limites\n")
    
    await message.add_reaction("1️⃣")
    await message.add_reaction("2️⃣")
    await message.add_reaction("3️⃣")

    def check_reaction(reaction, user):
        return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "1️⃣" or str(reaction.emoji == "2️⃣") or str(reaction.emoji == "3️⃣"))
    
    try:
        reaction, user = await client.wait_for("reaction_add", timeout = 10, check = check_reaction)
        if reaction.emoji == "1️⃣":
            await ctx.send("\nIci la soeur de Delphine s'est rendue ici plutôt victime de la situation. Ce faisant elle s'est oubliée.\
                            \n Si vous aviez dit cela, en faisant reposer la décision de votre mère sur le fait que votre soeur a fauté, vous auriez justifié son interprétation injuste sur vos capacités de conduite.\n \
                            \nDans une telle situation, je vous propose au contraire de parler directement et avec assertivité du problème de fond qui vous a blessé à votre mère sans utiliser l'acte de votre soeur comme justification\
                            proposer à votre mère de vous faire confiance quitte à lui démontrer vos capacités de conduite. Voici une ressource sur l'assertivité: https://www.youtube.com/watch?v=jJUXTz_1rZE")

        elif reaction.emoji == "2️⃣":
            await ctx.send("Si vous aviez été la soeur de Delphine, ici par tristesse pour vos parents ou par sens de la justice, vous avez pris leur rôle de parent en oubliant le vôtre, être leur fille.\
                        \nIl se trouve que pour garder votre énergie et réparer la situation qui est la vôtre, je vous propose de ne vous occuppez que du conflit qui est le vôtre.\
                        \nSi vos parents sont trop indulgents avec votre soeur, ce n'est pas à vous de les changer. En plus vous oubliez votre propre besoin pour qu'ils vous fassent confiance dans vos capacités: leur dire pourquoi vous trouvez que la situation est injuste vis à vis de vous et proposer de leur prouver que vous savez conduire en toute sécurité.")

        elif reaction.emoji == "3️⃣":
            await ctx.send("\nDans cette situation, si vous aviez répondu cela, vous auriez cru bien faire pour mettre des limites au comportement de votre soeur. \nMais au lieu de cela, vous récolterez le conflit durable avec votre soeur. Exprimez-lui plutôt les choses en utilisant des méthodes comme la CNV ou DESC. \nNe la jugez pas, ne la menaçez pas tout en exprimant ce pourquoi vous êtes en colère.\
                        \nVous pouvez aussi lui dire autrement que son comportement s'il s'envenime risque de nuir à la famille et à vous. https://www.youtube.com/watch?v=5HI4pSHEm1M")

    except:
        await ctx.send("Fin de la partie ! Veuillez recommencer")

client.run("OTc4NTcxMDAxODgzNDIyNzMx.G8UcSD.vDXZMSBgHJUS36FR2evBW4zIC4pz-E04Nw8UGw")