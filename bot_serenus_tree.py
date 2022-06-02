class Node :
    def __init__(self,question,keyword):
        self.question = question
        self.needs = '`Sommeil`\n`Equilibre émotionnel`\n`faire face à la dépression`\n`briser la solitude`'
        self.keyword = keyword
        self.list_child_node = []

    def user_response(self):
        print(self.question)
        print(self.needs)
        need = input()
        for child in self.list_child_node:
            if child.keyword in need:
                child.user_response()
            else:
                print("rentrer un des mots clés")

    def insert(self, node, question):
        if self.question == question :
            self.list_child_node.append(node)
                
        else:
            for child in self.list_child_node:
                child.insert(node,question)



# Tronc de l'arbre
Root = Node("Quels sont vos besoins ?","")


# Si il répond en branche Sommeil et que la question précèdente est bien le 2e argument alors on affiche le 1er agrument du Node entré en 1er argument
sleep = Root.insert(Node("Dites nous comment nous pouvons vous aider !","Sommeil"),"Quels sont vos besoins ?")

# Si choix de musique
music = Root.insert(Node("lien vers une musique pour le sommeil","musique"),"Dites nous comment nous pouvons vous aider !")

# Si choix de sophrologie
Root.insert(Node("lien vers le site de la sophrologie du sommeil","sophrologie du sommeil"),"Dites nous comment nous pouvons vous aider !")

# Si choix de podcast
Root.insert(Node("lien vers podcast assommant", "podcast"),"Dites nous comment nous pouvons vous aider !")

response = Root.user_response()

