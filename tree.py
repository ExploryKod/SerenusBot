class Node :
    def __init__(self,question,keyword):
        self.question = question
        self.keyword = keyword
        self.list_child_node = []

    def user_response(self):
        print(self.question)
        
        need = input()
        if need != "back":
            for child in self.list_child_node:
                if child.keyword in need:
                    print("on descend")
                    current_path.append(child)
                    print(current_path)
                    child.user_response()
            if child.keyword not in need:
                    print("renter un mot qui existe")
                    current_path[-1].user_response()

            

        elif need =="back":
             print("here")
             current_path.pop()
             print(current_path)
             current_path[-1].user_response()

        print("ici")
        

    def insert(self, node, question):
        if self.question == question :
            self.list_child_node.append(node)
        else:
            for child in self.list_child_node:
                child.insert(node,question)

# on met les questions dans des variables 

first_question_racine = "Quels sont vos besoins ?\nInsérez un de ces mots clés dans votre demande\n-sommeil\n-emotion\n-depression\n-solitude"
question_one_sommeil = "Dites nous comment nous pouvons vous aide pour que vous trouvez le sommeil? !\nLes mots clés: \nacupuncture\nmusique\nlithotherapie"
question_one_emotion = "Stress, angoisse, trop d'émotion\n Choisissez la méthode que vous voulez adopter !\nsophrologie\nconsultation\nconseils\nateliers\nmassage\nsport"
question_one_depression = "Choisissez une méthode pour faire face à la dépression\nphytotherapie\naromatherapie!"
question_one_solitude = "Afin de briser la solution , choisissez la methode que vous vouliez adopté: \ncombattez la négativité\nprenez soin des autres!"

# si choix est émotion
question_two_sophrologie = "Quels types d'exercices psychocorporelles ? : \nrespiration\nmaitriser son stress\nrevivre un moment de plaisir"
question_two_consultation = "Quelles types de consultations ? : \npsychologue\nnutritionniste\npsychiatre\npsychanaliste\nmagnetiseur\nnaturopathe"
question_two_conseils = "Avec un membre ou un professionnel ? : \nprofessionnel\nmembre"
question_two_ateliers = "Quelles genres d'ateliers voulez vous pratiquer ? : \nmusique\njeu intéractif\ncomedie\nmeditation"
question_two_massage = "Choissisez le type de massage ? : \nle massage shiatsu\nle massage thailandais"
question_two_sport = "Choissisez le type de sport? : \ncourse à pied\nendurance\nescalade"
#si choix est atelier
question_atelier_jeu = "Quels type de jeux ? : \nart thérapeutique\njeu de gestion de conflit\njeu de formulation d'un objectif SMART"
question_atelier_meditation = "Quels genre de méditations : \nyoga\nmeridienne\nature"
question_atelier_comedie = "Quels type de comedie : \nimprovisation théatrale\ncomedie musicale\ncomedie muette"

# présentez les réponses
answer_sommeil_acupuncture = "L'acupuncture est une médecine traditionnelle chinoise qui consiste à planter \ndes aiguilles dans des zones précises du corps afin d'en refaire circuler l'énergie.\n Prenez rendez-vous pour une seance de 30min ou 45min"
answer_sommeil_musique = ""
answer_sommeil_lithothérapie = ""



Root = Node("Dites help pour commencer l'étude","aide")

Root.insert(Node(first_question_racine,"help"),"Dites help pour commencer l'étude")
# =================      questions reponse pour gérer le sommeil
Root.insert(Node(question_one_sommeil,"sommeil"),first_question_racine)
# =================      questions reponse pour gérer l'équilibre émotionnelle
Root.insert(Node(question_one_emotion,"emotion"),first_question_racine)
# =================      questions reponse pour gérer la depression
Root.insert(Node(question_one_depression,"depression"),first_question_racine)
# =================      questions reponse pour gérer la solitude
Root.insert(Node(question_one_solitude,"solitude"),first_question_racine)


# ================================= PREMIERE CHOIX

# choix de réponse pour la gestion du sommeil
Root.insert(Node(answer_sommeil_acupuncture,"acupuncture"),question_one_sommeil)
Root.insert(Node("voici un lien contenant différent musique pour s'endormir : \n https://music.apple.com/fr/album/30-tracks-pour-dormir-sendormir-rapidement-relax-musique/1255567434","musique"),question_one_sommeil)
Root.insert(Node("La lithothérapie pour le sommeil mais également pour le bien-être en général, ou l’art \nde se soigner avec les pierres. C’est une médecine alternative liée à d’anciennes \ntraditions qui connaît aujourd’hui un regain d’intérêt pour régler certains troubles de façon totalement naturelle.\n Voici les différents pierres : \n L’améthyste \nl’hématite\nle quartz rose\n l’howlite \nla tourmaline","lithotherapie"),question_one_sommeil)


# choix de réponse pour la gestion des Emotions
Root.insert(Node(question_two_sophrologie,"sophrologie"),question_one_emotion)
Root.insert(Node(question_two_consultation,"consultation"),question_one_emotion)
Root.insert(Node(question_two_conseils,"conseils"),question_one_emotion)
Root.insert(Node(question_two_ateliers,"ateliers"),question_one_emotion)
Root.insert(Node(question_two_massage,"massage"),question_one_emotion)
Root.insert(Node(question_two_sport,"sport"),question_one_emotion)

# choix de réponse pour gerer la depression
Root.insert(Node("Il est donc vivement conseillé de consulter son médecin ou son pharmacien avant de prendre un traitement\nLes plantes pour traiter la dépression légére : \nLE MILLEPERTUIS \nLa rhodiole \n Si aucune amélioration ne se fait sentir après six semaines de traitement, une consultation médicale s’impose.","Phytothérapie"),question_one_depression)
Root.insert(Node("L’aromathérapie peut être utilisée pour vous aider à penser à autre chose et vous soulager.\n Voici quelques huiles essentielles : \nL’huile essentielle d’Orange Douce \nL’huile essentielle d’Ylang-Ylang \nL’huile essentielle de Lavande \nL’huile essentielle de Camomille Romaine \nL’huile essentielle de Marjolaine à Coquilles ","aromathérapie"),question_one_depression)

# choix de réponse pour briser la solitude
Root.insert(Node("Commencez par identifier les moments où vos croyances pessimistes ou vos jugements \ntrop critiques prennent le pas sur votre bienveillance et votre confiance dans la vie \net dans les autres. Puis, pour chacune de ces croyances ou constats négatifs, \nfaites-vous l'avocat du diable en vous efforçant de trouver un ou deux arguments \nqui viennent les contredire. Essayez ensuite de pratiquer un exercice de gratitude à la fin de chaque journée.","négativité"),question_one_solitude)
Root.insert(Node("Se sentir utile renforce la bonne estime de soi et change la dynamique relationnelle. \nC'est également la meilleure manière de sortir de l'isolement affectif et de renouer avec le sentiment d'appartenance à la communauté des hommes.","soin"),question_one_solitude)


# ==================== DEUXIEME PARTIE POUR GERER LES EMOTIONS : les branches
# dans chaque branche pour la gestion des émotions ses feuilles
# si la réponse est sophrologie
Root.insert(Node("Confortablement assise, je ferme les yeux et je prends conscience des différentes \nparties de mon corps : le front, le cou, le sternum, le ventre, le bas ventre. \nJe relâche progressivement mes muscles. J'inspire 4 secondes en gonflant mon ventre. \nJe bloque ma respiration durant 4 secondes. \nJ'expire en rentrant le ventre progressivement sur 4 secondes. \nJe bloque à nouveau ma respiration 4 secondes, \navant de reprendre un bol d'air et ma respiration habituelle.","respiration"),question_two_sophrologie)
Root.insert(Node("Confortablement assise ou allongée, \nje ferme les yeux, je me concentre sur ma respiration \net je visualise le déroulement d'une journée calme et détendue – \ndepuis le petit-déjeuner jusqu'au coucher.","S'imaginer au calme"),"Quels types d'exercices psychocorporelles ?")
Root.insert(Node("Confortablement assise sur une chaise, \nje ferme les yeux et je garde le dos bien droit. \nJe visualise une situation de stress que je vis régulièrement. \nEn respirant profondément, je m'imagine garder mon calme, accepter mes émotions, \nlâcher-prise vis-à-vis de mes angoisses... J'inspire durant plusieurs secondes et, \nà l'expiration, je laisse le bien-être qui en résulte se diffuser dans mon corps.","stress"),question_two_sophrologie)
Root.insert(Node("Confortablement assise ou allongée, je ferme les yeux et je sélectionne un moment de plaisir \nque j'ai vécu pour le revivre pleinement, en me concentrant sur les détails, \nsur les émotions ressenties et sur le bonheur de l'instant présent. \nJe réveille le ressenti des sensations agréables. Je prends le temps de \nbien poser le contexte. Je respire profondément et je m'étire.","plaisir"),question_two_sophrologie)
# si la réponse est consultation
Root.insert(Node("RDV psychologue","psychologue"),question_two_consultation)
Root.insert(Node("RDV nutritionniste","nutritionniste"),question_two_consultation)
Root.insert(Node("RDV psychiatre","psychiatre"),question_two_consultation)
Root.insert(Node("RDV psychannaliste","psychanaliste"),question_two_consultation)
Root.insert(Node("RDV naturopathe","naturopathe"),question_two_consultation)
Root.insert(Node("RDV magnétiseur","magnetiseur"),question_two_consultation)
# si la réponse est conseils
Root.insert(Node("RDV avec un professionnel\n","professionnel"),question_two_conseils)
Root.insert(Node("mettre en relation avec un membre","membre"),question_two_conseils)
# si la réponse est atelier
Root.insert(Node("Fermez les yeux ,allongez vous sur le dos et écoutez : \nhttps://www.youtube.com/watch?v=GHpksxJwRVw","musique"),question_two_ateliers)
Root.insert(Node(question_atelier_jeu,"jeu"),question_two_ateliers)
Root.insert(Node(question_atelier_meditation,"meditation"),question_two_ateliers)
Root.insert(Node(question_atelier_comedie,"comedie"),question_two_ateliers)
# dans jeu interactif
Root.insert(Node("art","art"),question_atelier_jeu)
Root.insert(Node("appel du jeu","conflit"),question_atelier_jeu)
Root.insert(Node("appel du jeu","SMART"),question_atelier_jeu)
# dans meditation
Root.insert(Node("séance yoga","yoga"),question_atelier_meditation)
Root.insert(Node("séance meridienne","meridienne"),question_atelier_meditation)
Root.insert(Node("Observons la nature","nature"),question_atelier_meditation)
# dans comedie
Root.insert(Node("lien de video théatre","improvisation"),question_atelier_comedie)
Root.insert(Node("lien comedie musicale","musicale"),question_atelier_comedie)
Root.insert(Node("lien comedie muette","muette"),question_atelier_comedie)
# si la réponse est massage
Root.insert(Node("shiatsu","shiatsu"),question_two_massage)
Root.insert(Node("Le thailandais","thailandais"),question_two_massage)
# si la réponse est sport
Root.insert(Node("course","course"),question_two_sport)
Root.insert(Node("endurance de 30min","endurance"),question_two_sport)
Root.insert(Node("faire une escalade","escalade"),question_two_sport)



current_path = [Root]
""" Root.user_response() """