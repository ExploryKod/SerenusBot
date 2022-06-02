
import discord
from tree import *

from ast import Try
client = discord.Client()

from discord.ext import commands

client = commands.Bot(command_prefix="")




@client.event
async def on_ready():
    print("Le bot est prêt.")



#lorsqu'on a un nouveau membre
@client.event
async def on_member_join(member):
    Help_channel = client.get_channel(978575214923350030)
    await Help_channel.send('Serenus vous souhaite la bienvenue !' + member.display_name)
    await Help_channel.send('Si vous voulez de l aide tapez : help' + member.display_name)
    await Help_channel.send('Si au cours de la  conversation vous voulez retourner en arriere tapez : back' + member.display_name)


@client.command()
async def serenus(ctx,arg):
    
    if arg != "back" and arg != "quit":
        for child in current_path[-1].list_child_node:
            if child.keyword in arg:
                current_path.append(child)
                await ctx.channel.send(child.question)
        if current_path[-1].keyword not in arg:
            await ctx.send("! Mettez dans votre requête un des mots clés émis")
            await ctx.channel.send(current_path[-1].question)
                
    elif arg == "back" and arg != "quit":
        current_path.pop()
        await ctx.channel.send(current_path[-1].question)

    elif arg == "quit" and arg != "back":
        await ctx.send("Vous n'êtes avez quittez la séance d'accompagnement\n Taper `serenus back` pour revenir en arriere ou `hello` pour retourner à l'accueil")



""" Game SMART """

@client.command()
async def smart(ctx):
    await ctx.send("Souvent, lorsque nous allons mal, nous formulons mal nos objectifs sans s'en rendre compte c'est à dire mentalement.")
    await ctx.send("Je vous propose ici de formuler consciement vos objectifs pour les rendre plus engageant c'est à dire que votre cerveau les écoutera plus et s'ensuivra l'action.")
    await ctx.send("Je vous présente donc trois objectifs, vous me dîtes en retour celui qui vous semble le mieux formulé. En retour, je vous donnerai de l'information pour améliorer les formulations.")
    await ctx.send("En retour, je vous donnerai de l'information pour améliorer les formulations.")
    await ctx.send("Voulez-vous jouer à ce jeu ? oui / non\n")

    def user_message(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel
    
    try:
        answer = await client.wait_for("message", timeout = 120, check = user_message)
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
        reaction, user = await client.wait_for("reaction_add", timeout = 120, check = check_reaction)
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

    


""" GAME Dialogue """

@client.command()
async def dialogue(ctx):
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
    
    message = await ctx.send("\n Avant de connaître les réponses: \nfermer les yeux et prenez la place de la soeur de Delphine, imaginez bien tous les détails et sentiments par empathie. \n Puis choississez la réponse ci-dessous la plus appropriée selon vous:\
                            \n\n1️⃣Vous allez voir vos parents pour leur dire: J'estime avoir le droit de prendre la voiture car ma soeur vient de la prendre et vous lui payez le permis en échange !\
                            \n\n2️⃣Vous allez voir vos parents pour leur dire:\nEn payant des cours à Delphine vous entrez dans une spirale, elle risque de faire d'autres conneries par la suite.Je crois au contraire qu'il faudrait être ferme mais juste.\
                            \n\n3️⃣Vous allez directement voir votre soeur pour lui dire avec un ton ferme: \
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



# fonction quand l'utilisateur veut supprimer un message
@client.event
async def on_message(message):
    message.content = message.content.lower()

    if message.author == client.user:
        return

    if message.content == "del":
        await message.channel.purge(limit=50)

    if message.content == "hello":
        await message.channel.send('Bienvenue dans Serenus Bot !')
        await message.channel.send('Nous avons pour but de vous aider à améliorer votre santé mentale')
        await message.channel.send('Voulez-vous en savoir plus ? plus/moins')

    if message.content == "plus":
        await message.channel.send('Si vous souhaitez être accompagnée dans votre cheminement psychique, écrivez: `serenus help`')
        await message.channel.send('et dans chacune de vos réponse mettez le mot `serenus` devant')
        await message.channel.send("si vous voulez accéder directement aux ressources")

        await message.channel.send("Voulez vous voir nos ressources ? tapez OK")

    if message.content == "ok":
        await message.channel.send("Voici une liste de nos ressources disponibles:")
        await message.channel.send("\n`phythothérapie` \n`aromathérapie` \n`stress` \n`panique` \n`dance` \n`musique` \n`lithothérapie` \nMusique pour s'endormir : `dormir` \n`acupuncture` \nMassage : `shiatsu` et le massage Chi Nei Tsang `massage` \n`respiration` \n Revivez des moment de plaisir `plaisir` \n Prenez soin des autres pour briser la solitude `soin`")
    

    await client.process_commands(message)





""" Les embeds """

@client.command()
async def phythothérapie(ctx):
    name = "La phythothérapie"
    description = "Certaines plantes sont prescrites pour soulager les épisodes de dépression légère à modérée. Attention, elles ne suffisent pas à traiter une dépression sévère ou prolongée. Un avis médical est donc nécessaire avant de les utiliser.Les plantes pour traiter la dépression légére : \nLE MILLEPERTUIS \nLa rhodiole \n Si aucune amélioration ne se fait sentir après six semaines de traitement, une consultation médicale s’impose."
    avatar = "https://media.istockphoto.com/photos/cannabis-marijuana-surgical-pliers-picture-id1127647653?b=1&k=20&m=1127647653&s=170667a&w=0&h=pU15bu5XOcfPJGQyYNkVRmOrdI6iAxUA2tAairiH8wk="

    embed = discord.Embed(
        title = name ,
        description = description,
        color = 0xffffff,
        url = "https://www.vidal.fr/maladies/psychisme/depression-adulte/phytotherapie-plantes.html#:~:text=Le%20millepertuis%20pour%20traiter%20une,d%C3%A9pressifs%20transitoires%2C%20l%C3%A9gers%20%C3%A0%20mod%C3%A9r%C3%A9s."
    )
    embed.set_thumbnail(url = avatar)
    embed.set_image(url= "https://media.istockphoto.com/photos/herbal-tea-and-flowers-rhodiola-rosea-picture-id495056499?b=1&k=20&m=495056499&s=170667a&w=0&h=x8aGsR4yA0-W6HXczQI7tvW72wAEYPvGWhSL6AwKZfs=")
    embed.set_footer(text = "Article réaliser par Farmata")

    await ctx.send(embed = embed)



@client.command()
async def aromathérapie(ctx):
    name = "L'aromathérapie"
    description = "La dépression est aujourd'hui considérée comme une maladie qui se traduit par la tristesse et plusieurs sentiments (ou symptômes) comme le désespoir, une perte du plaisir, de motivation, accompagnés de troubles alimentaires, du sommeil, l’impression de ne servir à rien, pour personne et dans les cas les plus avancés, avec des pensées morbides."
    avatar = "https://media.istockphoto.com/photos/still-life-closeup-of-a-tranquil-spa-arrangement-picture-id1325095289?b=1&k=20&m=1325095289&s=170667a&w=0&h=WN2MnFRkjm-Sb3Pqu6jeQj8wR2sNu3qCGi6TFptwOPA="

    embed = discord.Embed(
        title = name ,
        description = description,
        color = 0xCFC5A0,
        url = "https://www.skinjay.com/fr/blog/post/huile-essentielle-depression.html"
    )
    embed.set_thumbnail(url = avatar)
    embed.set_image(url= "https://media.istockphoto.com/photos/cozy-composition-with-an-air-humidifier-a-set-of-aromatic-oils-and-a-picture-id1298336127?b=1&k=20&m=1298336127&s=170667a&w=0&h=gm_UfI1_z-UsJTnTkzqjn6R11CiOuA34TW0EgJu_d94=")
    embed.set_footer(text = "Article réaliser par Farmata")

    await ctx.send(embed = embed)

@client.command()
async def optimisme(ctx):
    name = "Combattre la négativité"
    description = "Commencez par identifier les moments où vos croyances pessimistes ou vos jugements trop critiques prennent le pas sur votre bienveillance et votre confiance dans la vie et dans les autres. Puis, pour chacune de ces croyances ou constats négatifs, faites-vous l'avocat du diable en vous efforçant de trouver un ou deux arguments qui viennent les contredire. Essayez ensuite de pratiquer un exercice de gratitude à la fin de chaque journée. Repassez-vous le film du jour et repérez tous les petits moments qui ont été faciles, agréables ou enrichissants. Attardez-vous sur chacun d'eux en les revivant et remerciez. Vous pouvez aussi noter tous les jours sur un carnet trois de ces événements positifs. Au fil du temps, le regard que vous poserez sur le monde et les autres sera plus bienveillant. Votre envie de prendre votre place dans un monde moins hostile vous fera alors aller vers les autres plus facilement."
    avatar = "https://media.istockphoto.com/photos/loneliness-teenage-girls-picture-id1308753258?b=1&k=20&m=1308753258&s=170667a&w=0&h=37CIPQDwK_Ic50FLEm3bt3aakkyVwc7gL9pdeK2qJ-U="

    embed = discord.Embed(
        title = name ,
        description = description,
        color = 0x75B56A,
        url = "https://www.psychologies.com/Moi/Moi-et-les-autres/Solitude/Articles-et-Dossiers/6-habitudes-pour-lutter-contre-la-solitude"
    )
    embed.set_thumbnail(url = avatar)
    embed.set_image(url= "https://media.istockphoto.com/photos/beautiful-woman-meditates-on-a-poppy-field-at-sunset-picture-id1326797929?b=1&k=20&m=1326797929&s=170667a&w=0&h=haizLlUF1Jafrx4xR8EhAJPjFoBX5TSoGVpbrcDvJ3w=")
    embed.set_footer(text = "Article réaliser par Farmata")

    await ctx.send(embed = embed)


@client.command()
async def soin(ctx):
    name = "Prenez soin des autres"
    description = "L'isolement et le repli sur soi non volontaires sont des facteurs de dépression et d'altération de l'estime de soi. Plus on se sent exclu, moins on s'attribue de valeur personnelle et moins on se traite bien. Il est donc essentiel de recommencer à prendre soin de soi physiquement et émotionnellement avant de renouer avec les autres. Soignez votre apparence physique, pratiquez des activités physiques, sportives ou artistiques. Faites la liste de ce qui pourrait vous procurer du bien-être au quotidien. Et surtout, privilégiez les petits plaisirs, ceux que vous négligez au prétexte que « de toute façon, ce n'est pas ça qui changera votre vie ». Enfin, prenez le temps de lister vos compétences et talents divers (des plus petits aux plus importants) et relisez régulièrement votre liste pour rebooster votre confiance en vous."
    avatar = "https://media.istockphoto.com/photos/young-woman-sitting-on-edge-looks-out-at-view-picture-id1065043970?b=1&k=20&m=1065043970&s=170667a&w=0&h=R70KeDNbSHqkUpIvBMALGxMtBZMKIt2Svvggtpvebw0="

    embed = discord.Embed(
        title = name ,
        description = description,
        color = 0x75B56A,
        url = "https://www.psychologies.com/Moi/Moi-et-les-autres/Solitude/Articles-et-Dossiers/6-habitudes-pour-lutter-contre-la-solitude"
    )
    embed.set_thumbnail(url = avatar)
    embed.set_image(url= "https://media.istockphoto.com/photos/young-asian-yoga-students-stretching-in-yoga-class-stock-photo-picture-id1347223677?b=1&k=20&m=1347223677&s=170667a&w=0&h=QU3uRwOR0TEi3vsLLDqlefcKZNzlo8KIa8mbxXVLV2U=")
    embed.set_footer(text = "Article réaliser par Farmata")

    await ctx.send(embed = embed)

@client.command()
async def respiration(ctx):
    name = "Pratiquez la respiration abdominale"
    description = "Confortablement assise, je ferme les yeux et je prends conscience des différentes parties de mon corps : le front, le cou, le sternum, le ventre, le bas ventre. Je relâche progressivement mes muscles. J'inspire 4 secondes en gonflant mon ventre. Je bloque ma respiration durant 4 secondes. J'expire en rentrant le ventre progressivement sur 4 secondes. Je bloque à nouveau ma respiration 4 secondes, avant de reprendre un bol d'air et ma respiration habituelle."
    avatar = "https://media.istockphoto.com/photos/young-attractive-woman-in-upward-abdominal-lock-pose-home-inter-picture-id639190600?b=1&k=20&m=639190600&s=170667a&w=0&h=-9EbFaUFlMYKtFKi3EJLI2Il0TVCee8vgTTxiqJL2zU="

    embed = discord.Embed(
        title = name ,
        description = description,
        color = 0x75B56A,
        url = "https://photo.femmeactuelle.fr/stress-anxiete-des-exercices-de-sophrologie-faciles-a-faire-pour-mieux-gerer-ses-emotions-31246#pratiquer-la-respiration-abdominale-539282"
    )
    embed.set_thumbnail(url = avatar)
    embed.set_image(url= "https://media.istockphoto.com/photos/beautiful-attractive-young-woman-doing-yoga-stretching-exercising-at-picture-id1330355583?b=1&k=20&m=1330355583&s=170667a&w=0&h=Ujw27YftHUgUATo13OFJMFAOGFK5R-k4MYInwZ55Xxk=")
    embed.set_footer(text = "Article réaliser par Farmata")

    await ctx.send(embed = embed)

@client.command()
async def stress(ctx):
    name = "Maitriser son stress"
    description = "Confortablement assise sur une chaise, je ferme les yeux et je garde le dos bien droit. Je visualise une situation de stress que je vis régulièrement. En respirant profondément, je m'imagine garder mon calme, accepter mes émotions, lâcher-prise vis-à-vis de mes angoisses... J'inspire durant plusieurs secondes et, à l'expiration, je laisse le bien-être qui en résulte se diffuser dans mon corps."
    avatar = "https://media.istockphoto.com/photos/m-no-where-close-to-finishing-this-deadline-tonight-picture-id1304876683?b=1&k=20&m=1304876683&s=170667a&w=0&h=e6ifobU9Y3SLYsrv2ZOaz0v5kX-AgnAFzHzvtRAMtes="

    embed = discord.Embed(
        title = name ,
        description = description,
        color = 0x75B56A,
        url = "https://photo.femmeactuelle.fr/stress-anxiete-des-exercices-de-sophrologie-faciles-a-faire-pour-mieux-gerer-ses-emotions-31246#pratiquer-la-respiration-abdominale-539282"
    )
    embed.set_thumbnail(url = avatar)
    embed.set_image(url= "https://images.unsplash.com/photo-1502230831726-fe5549140034?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NTF8fHJlbGF4fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=600&q=60")
    embed.set_footer(text = "Article réaliser par Farmata")

    await ctx.send(embed = embed)

@client.command()
async def plaisir(ctx):
    name = "Revivre un moment de plaisir"
    description = "Confortablement assise ou allongée, je ferme les yeux et je sélectionne un moment de plaisir que j'ai vécu pour le revivre pleinement, en me concentrant sur les détails, sur les émotions ressenties et sur le bonheur de l'instant présent. Je réveille le ressenti des sensations agréables. Je prends le temps de bien poser le contexte. Je respire profondément et je m'étire."
    avatar = "https://media.istockphoto.com/photos/happy-indian-mother-having-fun-with-her-daughter-outdoor-family-and-picture-id1325578537?b=1&k=20&m=1325578537&s=170667a&w=0&h=lBs-GbtRYwxH8uBby3p0UEpJ0SuiDGMnT87rx_K51Cg="

    embed = discord.Embed(
        title = name ,
        description = description,
        color = 0x75B56A,
        url = "https://photo.femmeactuelle.fr/stress-anxiete-des-exercices-de-sophrologie-faciles-a-faire-pour-mieux-gerer-ses-emotions-31246#pratiquer-la-respiration-abdominale-539282"
    )
    embed.set_thumbnail(url = avatar)
    embed.set_image(url= "https://media.istockphoto.com/photos/sunflower-picture-id504431448?k=20&m=504431448&s=612x612&w=0&h=JSrQc6u6SEjCpJZC-nG2t5zcEnBT1hxTgcaFYZ092gs=")
    embed.set_footer(text = "Article réaliser par Farmata")

    await ctx.send(embed = embed)


@client.command()
async def yoga(ctx):
    name = "Séance de Yoga avec Noëlline"
    description = "Le Yoga intégral est ancestral et il est accessible à tous niveaux puisqu’il permet de décomposer les postures de manière à ce que l’enseignement s’adapte au corps et aux besoins de chacun."
    avatar = "https://www.pexels.com/photo/candles-and-incense-for-meditation-3822622/"

    embed = discord.Embed(
        title = name ,
        description = description,
        color = 0x8ACFEC,
        url = "https://www.wooskill.com/fr/offer/o-13771-cours-de-yoga-integrale-accessible-a-tous-niveaux"
    )
    embed.set_thumbnail(url = avatar)
    embed.set_image(url= "https://www.pexels.com/photo/woman-squatting-on-ground-while-raising-both-hands-2035066/")
    embed.set_footer(text = "Article réaliser par Farmata")

    await ctx.send(embed = embed)

@client.command()
async def méridienne(ctx):
    name = "Séance de Yoga avec Noëlline"
    description = "Le Yoga intégral est ancestral et il est accessible à tous niveaux puisqu’il permet de décomposer les postures de manière à ce que l’enseignement s’adapte au corps et aux besoins de chacun."
    avatar = "https://www.pexels.com/photo/candles-and-incense-for-meditation-3822622/"

    embed = discord.Embed(
        title = name ,
        description = description,
        color = 0x8ACFEC,
        url = "https://www.wooskill.com/fr/offer/o-13771-cours-de-yoga-integrale-accessible-a-tous-niveaux"
    )
    embed.set_thumbnail(url = avatar)
    embed.set_image(url= "https://www.pexels.com/photo/woman-squatting-on-ground-while-raising-both-hands-2035066/")
    embed.set_footer(text = "Article réaliser par Farmata")

    await ctx.send(embed = embed)


@client.command()
async def musique(ctx):
    name = "Musique Onde du bonheur"
    description = "Fermez les yeux ,allongez vous sur le dos et écoutez"
    avatar = "https://burst.shopifycdn.com/photos/musical-instruments-for-folk-music.jpg?width=746&format=pjpg&exif=1&iptc=1"

    embed = discord.Embed(
        title = name ,
        description = description,
        color = 0x8ACFEC,
        url = "https://mixkit.co/free-stock-music/ambient/"
    )
    embed.set_thumbnail(url = avatar)
    embed.set_image(url= "https://burst.shopifycdn.com/photos/harp-musical-instrument-in-shadows.jpg?width=746&format=pjpg&exif=1&iptc=1")
    embed.set_footer(text = "Article réaliser par Farmata")

    await ctx.send(embed = embed)




@client.command()
async def chi(ctx):
    name = "Le massage Chi Nei Tsang"
    description = "Le ventre est désigné dans la médecine chinoise comme le second cerveau Les Taoïstes considèrent qu’il est le siège de nos émotions. (le cerveau émotionnel).Le Chi Nei Tsang, dérivé du Qi Qong,  (littéralement Chi énergie et Nei Tsang organes). Le ventre est le lieu de stockage d’émotions non digérées Les énergies perverses prisonnières dans le corps, ont une influence évidente sur notre état physique et psychique,  à l’origine de tensions, malaises, dysfonctionnements et maladies. Entrer en contact avec les émotions enfouies, dissimulées voire niées et anciennes et qui, une fois reconnues et comprises, donne à l'homme des ressources pour opérer à des changements, à des ajustements nécessaires sur le plan physique, mental, émotionnel.IL vise à libérer les énergies négatives , bloquées concentrées dans l’abdomen et à harmoniser ses émotions,  à défaire des nœuds de rétablir bien-être et joie, de restaurer la détente et la vitalité rééquilibrer ses émotions, calmer le mental permettre à l énergie de couler à nouveau librement .Détendre notre ventre permet d'avancer dans la vie ! Le Chi Nei Tsang fortifie le système immunitaire et renforce la résistance aux maladies,(Les patients qui reçoivent des traitements de Chi Nei Tsang avant et après une opération chirurgicale se rétablissent mieux et plus rapidement)."
    avatar = "https://burst.shopifycdn.com/photos/massage-therapist-treating-woman.jpg?width=746&format=pjpg&exif=1&iptc=1"

    embed = discord.Embed(
        title = name ,
        description = description,
        color = 0x8ACFEC,
        url = "https://www.pausedouceheure.fr/pages/chi-nei-tsang-1/"
    )
    embed.set_thumbnail(url = avatar)
    embed.set_image(url= "https://burst.shopifycdn.com/photos/spa-massage-table-room.jpg?width=746&format=pjpg&exif=1&iptc=1")
    embed.set_footer(text = "Article réaliser par Farmata")

    await ctx.send(embed = embed)


@client.command()
async def shiatsu(ctx):
    name = "Le massage shiatsu"
    description = "Le soin Shiatsu agit sur les systèmes nerveux sympathique et parasympathique en fonction du type de pression exercée. Il permet ainsi la détente profonde du corps et de l'esprit."
    avatar = "https://burst.shopifycdn.com/photos/female-relaxing-at-spa.jpg?width=746&format=pjpg&exif=1&iptc=1"

    embed = discord.Embed(
        title = name ,
        description = description,
        color = 0x8ACFEC,
        url = "https://andywellbeing.wixsite.com/website/shiatsu"
    )
    embed.set_thumbnail(url = avatar)
    embed.set_image(url= "https://burst.shopifycdn.com/photos/spa-tools-and-decorations.jpg?width=746&format=pjpg&exif=1&iptc=1")
    embed.set_footer(text = "Article réaliser par Farmata")

    await ctx.send(embed = embed)


@client.command()
async def acupuncture(ctx):
    name = "L'acupuncture"
    description = "L'acupuncture est une médecine traditionnelle chinoise qui consiste à planter \ndes aiguilles dans des zones précises du corps afin d'en refaire circuler l'énergie.\n Prenez rendez-vous pour une seance de 30min ou 45min"
    avatar = "https://burst.shopifycdn.com/photos/bowl-of-flowers-on-stone.jpg?width=746&format=pjpg&exif=1&iptc=1"

    embed = discord.Embed(
        title = name ,
        description = description,
        color = 0x8ACFEC,
        url = "https://burst.shopifycdn.com/photos/spa-flatlay.jpg?width=746&format=pjpg&exif=1&iptc=1"
    )
    embed.set_thumbnail(url = avatar)
    embed.set_image(url= "https://burst.shopifycdn.com/photos/spa-tools-and-decorations.jpg?width=746&format=pjpg&exif=1&iptc=1")
    embed.set_footer(text = "Article réaliser par Farmata")

    await ctx.send(embed = embed)


@client.command()
async def dormir(ctx):
    name = "Musique pour s'endormir"
    description = "voici un lien contenant différent musique pour s'endormir"
    avatar = "https://burst.shopifycdn.com/photos/candle-burning-by-bubble-bath.jpg?width=746&format=pjpg&exif=1&iptc=1"

    embed = discord.Embed(
        title = name ,
        description = description,
        color = 0x8ACFEC,
        url = "https://music.apple.com/fr/album/30-tracks-pour-dormir-sendormir-rapidement-relax-musique/1255567434"
    )
    embed.set_thumbnail(url = avatar)
    embed.set_image(url= "https://burst.shopifycdn.com/photos/pug-sleeping-in.jpg?width=746&format=pjpg&exif=1&iptc=1")
    embed.set_footer(text = "Article réaliser par Farmata")

    await ctx.send(embed = embed)

@client.command()
async def lithothérapie(ctx):
    name = "La lithothérapie"
    description = "La lithothérapie pour le sommeil mais également pour le bien-être en général, ou l’art \nde se soigner avec les pierres. C’est une médecine alternative liée à d’anciennes \ntraditions qui connaît aujourd’hui un regain d’intérêt pour régler certains troubles de façon totalement naturelle.\n Voici les différents pierres : \n L’améthyste \nl’hématite\nle quartz rose\n l’howlite \nla tourmaline"
    avatar = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4tBGrpuIXs0ryjU5JICiyTX8QMiB8pkjFQQ&usqp=CAU"

    embed = discord.Embed(
        title = name ,
        description = description,
        color = 0x8ACFEC,
        url = "https://wakeupserenity.com/lithotherapie-pour-le-sommeil/?gclid=Cj0KCQjwnNyUBhCZARIsAI9AYlG9nTjFLExc7ib-HxNtqPY3rLZfvAfoSUiGcCwukrJDJE5B_qpjrMUaAjbAEALw_wcB"
    )
    embed.set_thumbnail(url = avatar)
    embed.set_image(url= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5FS6r9F_taeOYTiv7QEazWZRFfOtxu0HAJw&usqp=CAU")
    embed.set_footer(text = "Article réaliser par Farmata")

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
async def naturopathe(ctx):
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
async def psychanalyste(ctx):
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
async def panique(ctx):
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

    embed.set_thumbnail(url = "https://i.pinimg.com/originals/1b/e4/b2/1be4b2a8638a9b57e45fe8b518bb3c46.jpg") 
    embed.set_image(url = "https://www.superprof.fr/images/annonces/professeur-home-cours-salsa-bachata-kizomba-choregraphie-ouverture-bal-mariage.jpg")
    embed.set_footer(text="Auteur: {}".format(author))

    await ctx.send(embed = embed)


@client.command()
async def escalade(ctx):
    name = ctx.guild.name
    description = "Voici un lien vers une salle d'escalade, allez le découvrir!"

 
    url = "https://www.arkose.com/"
    author = "Amaury"

    embed = discord.Embed(
        title = name,
        url = url,
        description = description,
        color = discord.Color.green()
    )

    embed.set_thumbnail(url = "https://images.pexels.com/photos/6700827/pexels-photo-6700827.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
    embed.set_image(url = "https://images.pexels.com/photos/449609/pexels-photo-449609.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
    embed.set_footer(text="Auteur: {}".format(author))
    await ctx.send(embed = embed)


""" mettez le token de votre bot """
client.run("")