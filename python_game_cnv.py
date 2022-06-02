

def context_description(): 
    
    context = "SCENARIO: \n\nVous suprenez votre soeur Delphine, qui n'a pas de permis, en train de prendre seule la voiture familiale. \
            \nVotre mère aussi l'a vu en revenant de son trajet. Pour toute punition elle décide alors d'offrir à votre soeur une formation accélérée de conduite !\
            \nOr vous avez dû payer vous-même votre permis et n'avait pu faire la conduite accompagnée. \nVotre mère n'a pas confiance dans votre capacité à conduire sa voiture.\
            \n\nElle vous a interdit de conduire la voiture familiale car vous êtes \"trop maladroite\" alors que vous avez le permis depuis 2 mois."
    
    make_a_choice = "\nJe vous invite à lire les 3 propositions de réponses à donner à cette situation. Choississez celle qui s'approche de la meilleur voie pour adresser la situation en indiquant juste le chiffre entre parenthèse pour y répondre."

    return context+make_a_choice


def reactions():
    
    reaction_victim = " \n(1) Vous allez voir vos parents pour leur dire:\
                      - \" J'estime avoir le droit de prendre la voiture car ma soeur vient de la prendre et vous lui payez le permis en échange ! \"\n"
                      
    reaction_rescue = " \n(2) Vous allez voir vos parents pour leur dire:\
                      - \" \n En payant des cours à Delphine vous entrez dans une spirale, elle risque de faire d'autres conneries par la suite. \
                      Je crois au contraire qu'il faudrait être ferme mais juste: \
                      \n refusez-lui le passage du permis pendant 1 an du fait de sa faute puis offrez-lui les cours l'année d'aprés.\"\n "
                      
    reaction_predator = " \n(3) Vous allez directement voir votre soeur pour lui dire avec un ton ferme: \
                        \nTu as pris la voiture, sache que si tu recommence et que je suis la seule à le voir, je ne peux garder cela pour moi. \
                        \nJe serais bien obligé de le dire aux parents car cela mettra des limites\n"
    
    return "\nREPONSES\n"+reaction_victim+"\n"+reaction_rescue+"\n"+reaction_predator
     
                        
def bot_response(reaction_choice):
    
    response_victim = "\nIci la soeur de Delphine s'est rendue ici plutôt victime de la situation. Ce faisant elle s'est oubliée.\
                      \n Si vous aviez dit cela, en faisant reposer la décision de votre mère sur le fait que votre soeur a fauté, vous auriez justifié son interprétation injuste sur vos capacités de conduite.\n \
                          Dans une telle situation, je vous propose au contraire de parler directement et avec assertivité du problème de fond qui vous a blessé à votre mère sans utiliser l'acte de votre soeur comme justification, proposer à votre mère de vous faire confiance quitte à lui démontrer vos capacités de conduite."
    ressource_assertive = "https://www.youtube.com/watch?v=jJUXTz_1rZE"
    response_rescue = "Si vous aviez été la soeur de Delphine, ici par tristesse pour vos parents ou par sens de la justice, vous avez pris leur rôle de parent en oubliant le vôtre, être leur fille.\
                        \nIl se trouve que pour garder votre énergie et réparer la situation qui est la vôtre, je vous propose de ne vous occuppez que du conflit qui est le vôtre.\
                        \nSi vos parents sont trop indulgents avec votre soeur, ce n'est pas à vous de les changer. En plus vous oubliez votre propre besoin pour qu'ils vous fassent confiance dans vos capacités: leur dire pourquoi vous trouvez que la situation est injuste vis à vis de vous et proposer de leur prouver que vous savez conduire en toute sécurité."
    response_predator = "\nDans cette situation, si vous aviez répondu cela, vous auriez cru bien faire pour mettre des limites au comportement de votre soeur. \nMais au lieu de cela, vous récolterez le conflit durable avec votre soeur. Exprimez-lui plutôt les choses en utilisant des méthodes comme la CNV ou DESC. \nNe la jugez pas, ne la menaçez pas tout en exprimant ce pourquoi vous êtes en colère.\
                         \nVous pouvez aussi lui dire autrement que son comportement s'il s'envenime risque de nuir à la famille et à vous."
    ressource_cnv = "https://www.youtube.com/watch?v=5HI4pSHEm1M"
    
    if reaction_choice == 1:
        return response_victim + "\n" + ressource_assertive
    elif reaction_choice == 2:
        return response_rescue
    else:
        return response_predator + ressource_cnv

def play_dialogue_game_or_not():
    
    rules = "Bienvenue dans le jeu des rôles: apprenez à mieux résoudre un conflit au travers d'une histoire fictive. \
            \nVous serez mieux armé quand vous rencontrerez une situation similaire."
    
    print(rules)
    print("Voulez-vous jouer à ce jeu ? oui / non")
    user_trigger_game = input().lower()
    if user_trigger_game == "oui":
        dialogue_game()
    elif user_trigger_game == "non":
        print("Je comprends que vous n'ayez pas envie. Prenez bien soin de vous.") 
    else:
        print("Avez-vous bien tapé \"oui\" ou \"non\" sans espace ?")   
    
def dialogue_game():
      
    print(context_description())
    print("\n Avant de connaître les réponses: \nfermer les yeux et imaginer-vous en train de répondre avec le plus de détails possible.")
    print("\nUne fois que vous êtes prêt, écrivez 'oui' pour voir les réponses pré-définis ou écrivez autre chose pour sortir du jeu.")
    user_continue = input().lower()
    
    if user_continue == "oui":
        print(reactions())
        
        try:
            user_response_choice = int(input())

            if user_response_choice == 1:
                print(bot_response(1))
            elif user_response_choice == 2:
                print(bot_response(2))
            elif user_response_choice == 3:
                print(bot_response(3))
            else:
                print("\nTapez bien un chiffre de 1 à 3")
                print("\nNous relançons le descriptif du scénario et des réponses, choississez à nouveau.\n")
                dialogue_game()
        except:
            print("Vous devez taper un chiffre et non un mot pour que je comprenne votre choix.\n recommençons avec un chiffre:\n\n")
            dialogue_game()
    else:
        print("merci d'avoir participé jusque-là.")
        return
        
play_dialogue_game_or_not()
    
    
    