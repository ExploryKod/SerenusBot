# Faire le Bot

# @client.event
# async def on_message(message):
#     message.content = message.content.lower()
#     if message.author == client.user:
#         return
    
#     #Je copie l'identifiant de mon serveur par clique droit sur un salon (je dois être en mode développeur => voirn paramètres avancés de mon profil discord)
#     Help_channel = client.get_channel(978273051672207380)
    
#     #on met un symbole que l'on utilisera pas dans la discussion afin que le bot ne se déclenche pas si on dit 'help'
#     if message.channel == Help_channel and message.content.startswith('$help'):
#         await Help_channel.send('Bonjour!')
#     if message.content == 'del':
#         await message.channel.purge(limit=3)
    
#     await client.process_commands(message)




# Q_aide1 = "Bonjour, Quel est votre besoin ?"
# R_aide1 = ["(1)Trouver le sommeil", "(2)Equilibre émotionnelle", "(3)Faire face à la dépression", "(4)Briser la solitude"]

# sommeil = ["acupuncture", "musique", "podcasts", "lithothérapie"]
# emotion = ["sophrologie", "consultation", "conseils", "Méthode psychocorporelle", "Atelier", "Massage", "Sport"]
# depression = ["phytotherapie", "Aromathérapie", "sport", "lithothérapie", "Atelier", "sophrologie", "Methode psychocorporelle"]
# solitude = ["Sortie en groupe", "discussion"]


# response_sophrologie = {
#     "Respiration abdominale" : "Bien et toi",
#     "S'imaginer au calme" : "Hello",
#     "Maîtriser son stress" : "gdhj",
#     "Revivre un moment de plaisir": "hcn"
# }
# response_consultation = {
#     "Psychologue" : "Bien et toi",
#     "nutritionniste" : "Hello",
#     "Psychiatre" : "gdhj",
#     "Psychanaliste": "hcn",
#     "Naturopathe" : "gdhj",
#     "Magnétiseur" : "gdhj"
# }
# response_conseils = {
#     "Professionnel" : "Bien et toi",
#     "membre" : "Hello",
# }

# response_ateliers = {
#     "Art thérapeuthique" : "Bien et toi",
#     "Jeu interactif" : "Hello",
#     "Méditation" : "gdhj",
#     "Comedie": "hcn"
# }
# response_psychocorporelle = {
#     "Musique onde du bonheur" : "Bien et toi",
#     "Jeu interactif" : "Hello",
#     "Méditation" : "gdhj",
#     "Comedie": "hcn"
# }
# response_massage = {
#     "Musique onde du bonheur" : "Bien et toi",
#     "Jeu interactif" : "Hello",
#     "Méditation" : "gdhj",
#     "Comedie": "fancy_getopt"
# }


# reponse = {
#     "Musique onde du bonheur" : "Bien et toi",
#     "Jeu interactif" : "Hello",
#     "Méditation" : "gdhj",
#     "Comedie": "hcn"
# }

# besoin = input()

# while besoin != "Au revoir":
#     if besoin in reponse:
#         print(reponse[besoin])
#     else:
#         print("Je ne sais pas comment réagir, quelle serait la bonne réponse")
#         reponse[besoin] = input()
#         print("Merci, je m'en souviendrai et maintenant ?")
#     besoin = input()
# print("A plus")