
# choix de réponse pour la gestion des Emotions
Root.insert(Node("Quels types d'exercices psychocorporelles ?","Sophrologie", "retour"),"Dites nous comment nous pouvons vous aider !")
Root.insert(Node("Quelles types de consultations ?","Consultation", "retour"),"Dites nous comment nous pouvons vous aider !")
Root.insert(Node("Avec un membre ou un professionnel ?","Conseils","retour"),"Dites nous comment nous pouvons vous aider !")
Root.insert(Node("Quelles genres d'ateliers voulez vous pratiquer ?","Atelier", "retour"),"Dites nous comment nous pouvons vous aider !")
Root.insert(Node("Choissisez le type de massage ?","Massage", "retour"),"Dites nous comment nous pouvons vous aider !")
Root.insert(Node("Choissisez le type de sport?","Sport", "retour"),"Dites nous comment nous pouvons vous aider !")

# choix de réponse pour gerer la depression
Root.insert(Node("Il est donc vivement conseillé de consulter son médecin ou son pharmacien avant de prendre un traitement\nLes plantes pour traiter la dépression légére : \nLE MILLEPERTUIS \nLa rhodiole \n Si aucune amélioration ne se fait sentir après six semaines de traitement, une consultation médicale s’impose.","Phytothérapie"),"Dites nous comment nous pouvons vous aider !")
Root.insert(Node("L’aromathérapie peut être utilisée pour vous aider à penser à autre chose et vous soulager.\n Voici quelques huiles essentielles : \nL’huile essentielle d’Orange Douce \nL’huile essentielle d’Ylang-Ylang \nL’huile essentielle de Lavande \nL’huile essentielle de Camomille Romaine \nL’huile essentielle de Marjolaine à Coquilles ","aromathérapie"),"Dites nous comment nous pouvons vous aider !")

# choix de réponse pour briser la solitude
Root.insert(Node("Commencez par identifier les moments où vos croyances pessimistes ou vos jugements \ntrop critiques prennent le pas sur votre bienveillance et votre confiance dans la vie \net dans les autres. Puis, pour chacune de ces croyances ou constats négatifs, \nfaites-vous l'avocat du diable en vous efforçant de trouver un ou deux arguments \nqui viennent les contredire. Essayez ensuite de pratiquer un exercice de gratitude à la fin de chaque journée.","Combattez la négativité"),"Dites nous comment nous pouvons vous aider !")
Root.insert(Node("Se sentir utile renforce la bonne estime de soi et change la dynamique relationnelle. \nC'est également la meilleure manière de sortir de l'isolement affectif et de renouer avec le sentiment d'appartenance à la communauté des hommes.","Prenez soin des autres"),"Dites nous comment nous pouvons vous aider !")



# ==================== DEUXIEME PARTIE POUR GERER LES EMOTIONS : les branches
# dans chaque branche pour la gestion des émotions ses feuilles
# si la réponse est sophrologie
Root.insert(Node("Confortablement assise, je ferme les yeux et je prends conscience des différentes \nparties de mon corps : le front, le cou, le sternum, le ventre, le bas ventre. \nJe relâche progressivement mes muscles. J'inspire 4 secondes en gonflant mon ventre. \nJe bloque ma respiration durant 4 secondes. \nJ'expire en rentrant le ventre progressivement sur 4 secondes. \nJe bloque à nouveau ma respiration 4 secondes, \navant de reprendre un bol d'air et ma respiration habituelle.","respiration"),"Quels types d'exercices psychocorporelles ?")
Root.insert(Node("Confortablement assise ou allongée, \nje ferme les yeux, je me concentre sur ma respiration \net je visualise le déroulement d'une journée calme et détendue – \ndepuis le petit-déjeuner jusqu'au coucher.","S'imaginer au calme"),"Quels types d'exercices psychocorporelles ?")
Root.insert(Node("Confortablement assise sur une chaise, \nje ferme les yeux et je garde le dos bien droit. \nJe visualise une situation de stress que je vis régulièrement. \nEn respirant profondément, je m'imagine garder mon calme, accepter mes émotions, \nlâcher-prise vis-à-vis de mes angoisses... J'inspire durant plusieurs secondes et, \nà l'expiration, je laisse le bien-être qui en résulte se diffuser dans mon corps.","maîtriser son stress"),"Quels types d'exercices psychocorporelles ?")
Root.insert(Node("Confortablement assise ou allongée, je ferme les yeux et je sélectionne un moment de plaisir \nque j'ai vécu pour le revivre pleinement, en me concentrant sur les détails, \nsur les émotions ressenties et sur le bonheur de l'instant présent. \nJe réveille le ressenti des sensations agréables. Je prends le temps de \nbien poser le contexte. Je respire profondément et je m'étire.","revivre un moment de plaisir"),"Quels types d'exercices psychocorporelles ?")
# si la réponse est consultation
Root.insert(Node("RDV psychologue","Psychologue"),"Quelles types de consultations ?")
Root.insert(Node("RDV nutritionniste","nutritionniste"),"Quelles types de consultations ?")
Root.insert(Node("RDV psychiatre","Psychiatre"),"Quelles types de consultations ?")
Root.insert(Node("RDV psychannaliste","Psychanaliste"),"Quelles types de consultations ?")
Root.insert(Node("RDV naturopathe","Naturopathe"),"Quelles types de consultations ?")
Root.insert(Node("RDV magnétiseur","Magnétiseur"),"Quelles types de consultations ?")
# si la réponse est conseils
Root.insert(Node("RDV avec un professionnel","Professionnel"),"Avec un membre ou un professionnel ?")
Root.insert(Node("mettre en relation avec un membre","membre"),"Avec un membre ou un professionnel ?")
# si la réponse est atelier
Root.insert(Node("Fermez les yeux ,allongez vous sur le dos et écoutez : \nhttps://www.youtube.com/watch?v=GHpksxJwRVw","Musique onde du bonheur"),"Quelles genres d'ateliers voulez vous pratiquer ?")
Root.insert(Node("Quels type de jeux ?","Jeu interactif"),"Quelles genres d'ateliers voulez vous pratiquer ?")
Root.insert(Node("Quels genre de méditations","Méditation"),"Quelles genres d'ateliers voulez vous pratiquer ?")
Root.insert(Node("Quels type de comedie","Comedie"),"Quelles genres d'ateliers voulez vous pratiquer ?")
# dans jeu interactif
Root.insert(Node("art","Art thérapeuthique"),"Quels type de jeux ?")
Root.insert(Node("liste d'instrument","Instrument"),"Quels type de jeux ?")
Root.insert(Node("Cuisine","Gastronomie"),"Quels type de jeux ?")
# dans meditation
Root.insert(Node("séance yoga","Yoga"),"Quels genre de méditations")
Root.insert(Node("séance meridienne","Méridienne"),"Quels genre de méditations")
Root.insert(Node("Observons la nature","nature"),"Quels genre de méditations")
# si la réponse est massage
Root.insert(Node("shiatsu","Massage shiatsu"),"Choissisez le type de massage ?")
Root.insert(Node("Le thailandais","Massage thailandais"),"Choissisez le type de massage ?")
# si la réponse est sport
Root.insert(Node("course","course à pied"),"Choissisez le type de sport?")
Root.insert(Node("endurance de 30min","l'endurance"),"Choissisez le type de sport?")
Root.insert(Node("faire une escalade","l'escalade"),"Choissisez le type de sport?")



# =================      questions reponse pour gérer l'équilibre émotionnelle
Root.insert(Node("Briser la solitude ?","Solitude"),"Quels sont vos besoins ?")
# briser la solitude
Root.insert(Node("idée d'événement","Sorti en groupe"),"Briser la solitude ?")
Root.insert(Node("mettre en relation avec un membre","Discussion"),"Briser la solitude ?")
