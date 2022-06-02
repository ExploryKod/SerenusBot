from MyBot import Bot
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
        else:
             print("here")
             current_path.pop()
             print(current_path)
             current_path[-1].user_response()

      
    def insert(self, node, question):
        if self.question == question :
            self.list_child_node.append(node)
        else:
            for child in self.list_child_node:
                child.insert(node,question)


# 1er noeud (noeud racine)
Root = Node("Quels sont vos besoins ? \nSommeil\n Emotions\n Depression\n Solitude","help")
# =================      questions reponse pour gérer le sommeil
Root.insert(Node("Dites nous comment nous pouvons vous aider à mieux dormir ! Ecrivez une des options: \nacupuncture, musique ou lithotherapie","sommeil"),"Quels sont vos besoins ? \nSommeil\n Emotions\n Depression\n Solitude")
# =================      questions reponse pour gérer l'équilibre émotionnelle
Root.insert(Node("Dites nous comment nous pouvons vous aider à mieux vivre vos émotions !","emotion"),"Quels sont vos besoins ? \nSommeil\n Emotions\n Depression\n Solitude")
# =================      questions reponse pour gérer la depression
Root.insert(Node("Dites nous comment nous pouvons vous aider pour faire face à la dépression !","depression"),"Quels sont vos besoins ? \nSommeil\n Emotions\n Depression\n Solitude")
# =================      questions reponse pour gérer la solitude
Root.insert(Node("Dites nous comment nous pouvons vous aider à sortir de la solitude !","solitude"),"Quels sont vos besoins ? \nSommeil\n Emotions\n Depression\n Solitude")


# ================================= PREMIERE CHOIX

description_acupuncture = "L'acupuncture est une médecine traditionnelle chinoise qui consiste à planter \ndes aiguilles dans des zones précises du corps afin d'en refaire circuler l'énergie.\n Prenez rendez-vous pour une seance de 30min ou 45min\n Trouvez un acupuncteur: https://www.doctolib.fr/acupuncteur"
music_ressource = "voici un lien contenant différent musique pour s'endormir : \n https://music.apple.com/fr/album/30-tracks-pour-dormir-sendormir-rapidement-relax-musique/1255567434"
lithotherapie_description = "La lithothérapie pour le sommeil mais également pour le bien-être en général, ou l’art \nde se soigner avec les pierres. C’est une médecine alternative liée à d’anciennes \ntraditions qui connaît aujourd’hui un regain d’intérêt pour régler certains troubles de façon totalement naturelle.\n Voici les différents pierres : \n L’améthyste \nl’hématite\nle quartz rose\n l’howlite \nla tourmaline\
                            \n Plus d'information ici: https://www.france-mineraux.fr/lithosphere/quelles-pierres-utiliser-en-cas-de-trouble-du-sommeil/"

# choix de réponse pour la gestion du sommeil
Root.insert(Node(description_acupuncture,"acupuncture"),"Dites nous comment nous pouvons vous aider à mieux dormir ! Ecrivez une des options: \nacupuncture, musique ou lithotherapie")
Root.insert(Node(music_ressource,"musique"),"Dites nous comment nous pouvons vous aider à mieux dormir ! Ecrivez une des options: \nacupuncture, musique ou lithotherapie")
Root.insert(Node(lithotherapie_description,"lithotherapie"),"Dites nous comment nous pouvons vous aider à mieux dormir ! Ecrivez une des options: \nacupuncture, musique ou lithotherapie")

current_path=[Root]
