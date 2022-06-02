

def bad_goals(goal):
    
    if goal == 1:
        goal_vague= "(1) Aller à la plage cet aprés-midi pour réduire mon anxiété"
        return goal_vague
    elif goal == 2:
        goal_scheduled = "(2) Réduire mon anxiété en pratiquant un exercice tous les matin à 7h avant de partir"
        return goal_scheduled
    elif goal == 3:
        goal_specific = "(3) Réduire mon anxiété en utilisant l'exercice de pranayama, la respiration inversée. Mon anxiété sera réduite si je me sens bien dans mon corps."
        return goal_specific

def critics_goal(goal_pbm):
    
    print("\nVoici pourquoi c'est mal formulé:")
    
    if goal_pbm == 1:
        critics = "\nCe but n'est pas assez spécifique car nous ne savons pas quelle est la plage, ni l'heure précise d'engagement. \
                    \nIl lui manque aussi des informations sur l'action précise pour réduire votre anxiété. \
                    \nAssurez-vous aussi qu'il est réaliste: \nvous pouvez vous déplacer à la plage et rien de vous y empêche (travail etc...)\
                    \nAjoutez donc une heure ou une plage horaire: \nimaginer aussi en détail la scène de détente et engagez-vous par écrit à la réaliser.\
                    \nTrouver enfin un indicateur de satisfaction pour mesurer la baisse de votre anxiété aprés la plage." 
        return critics
    elif goal_pbm == 2: 
        critics = "\nCe but facilite l'engagement car il indique un rythme à un moment précis.\
                    \nIl lui manque en revanche de la spécificité car votre cerveau a besoin de se représenter en image précisément ce que vous allez faire.\
                    \nCette condition est importante pour se donner une réelle motivation à agir. \nAussi, comment savez-vous que votre anxiété a baissé ? Trouver un indicateur de satisfaction." 
        return critics
    elif goal_pbm == 3:
        critics = "\n La formulation ici permet au cerveau de bien se représenter la méthode utilisée pour atteindre l'objectif et il est réaliste. Il y a aussi un critère de satisfaction.\
                    \nCette formulation gagnerait à s'améliorer si vous ajoutez par exemple une horaire, un rythme ou un évènement pour vous engagez à pratiquer à ce moment.\
                    \nLe critère de satisfaction peut être améliorer pour mieux visualiser ce qui se passe dans le corps si l'objectif est atteint."
        return critics

def play_goal_game_or_not(num):
    
    rules = "\nSouvent, lorsque nous allons mal, nous formulons mal nos objectifs sans s'en rendre compte c'est à dire mentalement. \
        \nJe vous propose ici de formuler consciement vos objectifs pour les rendre plus engageant c'est à dire que votre cerveau les écoutera plus et s'ensuivra l'action.\
        \nJe vous présente donc trois objectifs, vous me dîtes en retour celui qui vous semble le mieux formulé. En retour, je vous donnerai de l'information pour améliorer les formulations."
    
    if num == 1:
        print("Nous vous remercions d'avoir joué")
        return
    else:
        print(rules)
    
        print("Voulez-vous jouer à ce jeu ? oui / non")
        user_want_play = input().lower()
        
        if user_want_play == "oui":
            goal_game()
        elif user_want_play == "non":
            print("Je comprends que vous n'ayez pas envie. Prenez bien soin de vous.") 
            return
        else:
            print("Avez-vous bien tapé \"oui\" ou \"non\" sans espace ?")  
            play_goal_game_or_not(0) 
    
def goal_game():
      
    print("Voici les 3 objectifs, répondez en utilisant un des chiffres mentionnés:")
    print(bad_goals(1))
    print(bad_goals(2))
    print(bad_goals(3))
    
  
    user_choice = int(input())

    if user_choice == 1:
        print(critics_goal(1))
        print("Ecrivez \"quittez\" si vous désirez quittez le jeu, sinon écrivez \"rejouer\"")
        stop = input().lower()
        if (stop == "rejouer"):
            goal_game()
        else:
            play_goal_game_or_not(1)
    elif user_choice == 2:
        print(critics_goal(2))
        print("Ecrivez \"quittez\" si vous désirez quittez le jeu, sinon écrivez \"rejouer\"")
        stop = input().lower()
        if (stop == "rejouer"):
            goal_game()
        else:
            play_goal_game_or_not(1)
    elif user_choice == 3:
        print(critics_goal(3))
        print("Ecrivez \"quittez\" si vous désirez quittez le jeu, sinon écrivez \"rejouer\"")
        stop = input().lower()
        if (stop == "rejouer"):
            goal_game()
        else:
            play_goal_game_or_not(1)
    else:
        print("\nTapez bien un chiffre de 1 à 3")
        print("\nNous relançons le descriptif du scénario et des réponses, choississez à nouveau.\n")
        goal_game()
    

play_goal_game_or_not(0)