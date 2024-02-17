class Node :
    def __init__(self,question,keyword):
        self.question = question
        self.keyword = keyword
        self.list_child_node = []

        
    def insert(self, node, question):
        if self.question == question :
            self.list_child_node.append(node)
        else:
            for child in self.list_child_node:
                child.insert(node,question)

# on met les questions dans des variables 

first_question_racine = "Quels sont vos besoins ?\nInsérez un de ces mots clés dans votre demande\n-`sommeil`\n-`emotion`\n-`depression`\n-`solitude`"
question_one_sommeil = "Dites nous comment nous pouvons vous aide pour que vous trouvez le sommeil? !\nLes mots clés: \n`acupuncture`\n`musique`\n`lithothérapie`"
question_one_emotion = "Stress, angoisse, trop d'émotion\n Choisissez la méthode que vous voulez adopter !\n `sophrologie`\n `consultation`\n `ateliers`\n `massage`\n `sport`"
question_one_depression = "Choisissez une méthode pour faire face à la dépression\n `phytotherapie`\n `aromatherapie`!"
question_one_solitude = "Afin de briser la solution , choisissez la methode que vous vouliez adopté: \n`optimisme`\nprenez `soin` des autres!"

# si choix est émotion
question_two_sophrologie = "Quels types d'exercices psychocorporelles ? : \n `respiration`\n maitriser son `stress`\nrevivre un moment de `plaisir` s'imaginer au calme"
question_two_consultation = "Quelles types de consultations ? : \n `psychologue`\n `nutritionniste`\n `psychiatre`\n `psychanalyste`\n `magnetiseur`\n `naturopathe`"

question_two_ateliers = "Quelles genres d'ateliers voulez vous pratiquer ? : \n `musique`\n `jeu` intéractif\n `meditation`"
question_two_massage = "Choissisez le type de massage ? : \nle massage `shiatsu`\nle massage `chi_nei_tsang`"
question_two_sport = "Choissisez le type de sport? : \n`dance`\nescalade"
#si choix est atelier
question_atelier_jeu = "Quels type de jeux ? : \njeu de gestion de `conflit`\njeu de formulation d'un objectif `smart`"




Root = Node("Dites help pour commencer l'étude","help")

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
Root.insert(Node("Ecrivez : acupuncture","acupuncture"),question_one_sommeil)
Root.insert(Node("Ecrivez : dormir","musique"),question_one_sommeil)
Root.insert(Node("Ecrivez : lithothérapie","lithothérapie"),question_one_sommeil)


# choix de réponse pour la gestion des Emotions
Root.insert(Node(question_two_sophrologie,"sophrologie"),question_one_emotion)
Root.insert(Node(question_two_consultation,"consultation"),question_one_emotion)

Root.insert(Node(question_two_ateliers,"ateliers"),question_one_emotion)
Root.insert(Node(question_two_massage,"massage"),question_one_emotion)
Root.insert(Node(question_two_sport,"sport"),question_one_emotion)

# choix de réponse pour gerer la depression
Root.insert(Node("Ecrivez : phythothérapie","phytothérapie"),question_one_depression)
Root.insert(Node("Ecrivez : aromathérapie","aromathérapie"),question_one_depression)

# choix de réponse pour briser la solitude
Root.insert(Node("Ecrivez : optimisme","optimisme"),question_one_solitude)
Root.insert(Node("Ecrivez : soin","soin"),question_one_solitude)


# ==================== DEUXIEME PARTIE POUR GERER LES EMOTIONS : les branches
# dans chaque branche pour la gestion des émotions ses feuilles
# si la réponse est sophrologie
Root.insert(Node("Ecrivez : respiration","respiration"),question_two_sophrologie)
Root.insert(Node("Ecrivez : stress","stress"),question_two_sophrologie)
Root.insert(Node("Ecrivez : plaisir","plaisir"),question_two_sophrologie)
# si la réponse est consultation
Root.insert(Node("Ecrivez : psychologue","psychologue"),question_two_consultation)
Root.insert(Node("Ecrivez : nutritionniste","nutritionniste"),question_two_consultation)
Root.insert(Node("Ecrivez : psychiatre","psychiatre"),question_two_consultation)
Root.insert(Node("Ecrivez : psychanalyste","psychanalyste"),question_two_consultation)
Root.insert(Node("Ecrivez : naturopathe","naturopathe"),question_two_consultation)
Root.insert(Node("Ecrivez : magnétiseur","magnetiseur"),question_two_consultation)

# si la réponse est atelier
Root.insert(Node("Ecrivez : musique","musique"),question_two_ateliers)
Root.insert(Node(question_atelier_jeu,"jeu"),question_two_ateliers)
Root.insert(Node("Ecrivez : yoga","meditation"),question_two_ateliers)

# dans jeu interactif
Root.insert(Node("Ecrivez pour lancer le jeu : smart","smart"),question_atelier_jeu)
Root.insert(Node("Ecrivez pour lancer le jeu : dialogue","conflit"),question_atelier_jeu)

# si la réponse est massage
Root.insert(Node("Ecrivez : shiatsu","shiatsu"),question_two_massage)
Root.insert(Node("Ecrivez : chi", "chi_nei_tsang"),question_two_massage)
# si la réponse est sport
Root.insert(Node("Ecrivez : dance","dance"),question_two_sport)
Root.insert(Node("Ecrivez : escalade","escalade"),question_two_sport)







current_path = [Root]
