from fonction_de_base import*

def tokenisation(question):
    question_formater = conversion_car(question)
    liste_mots = question_formater.split()
    return liste_mots

def recherche_mot_question(liste,directory):
    fichiers = os.listdir(directory)
    contenu_global=[]
    liste2=[]
    for nom in fichiers:
        with open(os.path.join(directory, nom), "r",encoding='utf-8') as fichier:  # On effectue un parcourt de chaque fichier un par un
            texte = fichier.read()  # la variable texte contient le contenu du fichier parcouru
            list_texte = texte.split()
        contenu_global += list_texte
    for mot in liste:
        if mot in contenu_global:
            liste2.append(mot)
    return liste2
    
res= transposee(matrice_tf_idf('cleaned'))
for elem in res:
    for val in elem:
        print(val, end="\t")
    print()
