import os
from math import *
"""OK: FONCTION RETOURNANT LA LISTE DES FICHIER D'UN REPERTOIRE"""
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def extraction_nom():
    noms=""
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")
    liste_noms=[]
    set_noms = set()
    for i in range(len(files_names)):
        noms=files_names[i]
        noms=noms[11:-4]
        if noms[-1] == '1' or noms[-1]=='2':
            noms=noms[:-1]
        for lettre in noms:
            if 0 <= ord(lettre)<= 9 :
                noms=liste_noms[:-1]
        liste_noms.append(noms)

    return liste_noms

def noms_prenoms(liste_noms):
    dictionnaire_presidents={}
    for nom in liste_noms:
        if nom == 'Macron':
            dictionnaire_presidents[nom]='Emmanuel'
        elif nom == 'Sarkozy':
            dictionnaire_presidents[nom]='Nicolas'
        elif nom == 'Chirac':
            dictionnaire_presidents[nom]='Jacques'
        elif nom =='Giscard dEstaing':
            dictionnaire_presidents[nom]='Valérie'
        elif nom =='Hollande'or nom=='Mitterand':
            dictionnaire_presidents[nom]='François'
    return dictionnaire_presidents

def conversion_car(texte):
    nv_texte=""
    liste_caractere=[',','.',':','?',';','!','-',"'",chr(34)]
    for caractere in texte:
        if 'A' <= caractere <= 'Z':
            nv_texte += chr(ord(caractere)+32)
        elif caractere in liste_caractere:
            nv_texte += ' '
        else:
            nv_texte += caractere
    return nv_texte

def occur(chaine): # fonction donnant l'occurrence de chaque mot d'une chaîne de caractères
    liste_mot = chaine.split()
    liste_compteur = []
    liste_test = []
    i = 0
    while i <= len(liste_mot) - 1:
        if liste_mot[i] not in liste_test:
            liste_test.append(liste_mot[i])
            compteur = 0
            for j in liste_mot:
                if liste_mot[i] == j:
                    compteur += 1
            liste_compteur.append(compteur)
        i += 1
    dico = dict(zip(liste_mot, liste_compteur))
    return dico


def tf(fichier): #prend en paramètre un dico ayant pour clé un mot et en valeur son nombre d'occurence et retourne son score tf
    with open(fichier,"r", encoding = 'utf-8') as fichier:
        texte = fichier.read()
        nb_mots = len(set(texte.split()))
        dico_occur = occur(texte)
        for cle, valeur in dico_occur.items():
            dico_occur[cle] = valeur/nb_mots
    return dico_occur

def tf_texte(texte):
    nb_mots=len(set(texte.split()))
    dico_occur = occur(texte)
    for cle, valeur in dico_occur.items():
        dico_occur[cle]= valeur/nb_mots
    return dico_occur

def idf(directory):
    fichiers = os.listdir(directory)
    liste_dico = []
    for nom in fichiers:
        texte = ""
        with open(os.path.join(directory, nom), "r", encoding='utf-8') as fichier:
            for ligne in fichier:
                texte += ligne
            liste_dico.append(occur(texte))

    liste_cle = []
    for dico in liste_dico:
        for cle in dico.keys():
            liste_cle.append(cle)

    ch_cle = ""
    for mot in liste_cle:
        ch_cle += mot + " "

    dico_idf = {}  # création du dictionnaire idf
    liste_chaine = ch_cle.split()
    for mot in liste_chaine:
        dico_idf[mot] = 0

    for i in range(len(liste_chaine)):
        oc = 0
        for val in liste_chaine:
            if liste_chaine[i] == val:
                oc += 1
        dico_idf[liste_chaine[i]] = oc

    nb = len(liste_dico)
    for cle, valeur in dico_idf.items():
        nv_valeur = log(((nb / valeur) + 1), 10)
        dico_idf[cle] = nv_valeur
    return dico_idf

def transposee(matrice):
    result_matrix = []

    for col in range(len(matrice[0])):
        line_matrix = []
        for line in range(len(matrice)):
            line_matrix.append(matrice[line][col])
        result_matrix.append(line_matrix)

    return result_matrix

def matrice_tf_idf(directory):
    matrice = []  # Initialisation de la matrice TF-IDF
    mots_uniques = list(idf(directory).keys())  # Liste de tous les mots uniques de tous les fichiers
    ligne_1 = ["Les mots: "]

    for mot in mots_uniques:
        ligne_1.append(mot)  # liste de tous les mots uniques de tous les fichiers
    matrice.append(ligne_1)  # on ajoute une première liste dans la matrice avec tous les mots
    score_idf = idf(directory)  # on affecte le score idf de tous les mots du répertoire dans un dictionnaire

    for file in list_of_files(directory,"txt"):
        colonne_1 = [file]
        file ='cleaned/'+file
        # initialisation de la colonne avec le nom du fichier
        score_tf = tf(file)# calcul des scores tf pour le fichier actuel
        score_tf_idf = {}  # initialisation d'un dictionnaire qui va associer à chaque mot du repertoire son score TF-IDF
        for mot in score_idf.keys():
            if mot in score_tf.keys():
                score_tf_idf[mot] = score_tf[mot] * score_idf[mot]
            else:  # si le mot n'est contenu dans aucun fichier alors son score tf idf est nul
                score_tf_idf[mot] = 0.0
        # Création de la ligne de la matrice pour ce fichier avec les scores TF-IDF
        ligne_score_tf_idf = colonne_1
        for score in score_tf_idf.values():
            ligne_score_tf_idf.append(score)

        matrice.append(ligne_score_tf_idf)  # ajout de la ligne à la matrice
    return (transposee(matrice))  # retrour de la matrice transposée
#print(matrice_tf_idf('cleaned'))


def mot_tf_idf_min(directory):    # fonction permettant de retourner les mots les moins importants
    matrice = matrice_tf_idf(directory)     # matrice contenant le tf-idf de directory
    dico_moy_idf = {}   # création d'un dictionnaire vide
    liste_mot=[]
    for i in range(1, len(matrice) - 1):
        somme_idf = 0 # création d'une fonction destiné à contenir la somme des tf-idf d'un mot
        moyenne=0
        for j in range(1, len(matrice[i]) - 1):
            somme_idf += matrice[i][j]
        moyenne = somme_idf/(len(matrice[i])-1)
        dico_moy_idf[matrice[i][0]]=moyenne
    mini = 1
    liste_mot_moins_important=[]
    for valeur in dico_moy_idf.values():
        if valeur<mini:
            mini = valeur
    for cle in dico_moy_idf.keys():
        if dico_moy_idf[cle]==mini:
            liste_mot_moins_important.append(cle)
    return liste_mot_moins_important


def mot_tf_idf_max(directory):
    matrice = matrice_tf_idf(directory)   # matrice contenant le tf-idf de directory"""
    dico_moy_idf = {}   # création d'un dictionnaire vide
    liste_mot=[]
    for i in range(1, len(matrice) - 1):
        somme_idf = 0 # création d'une fonction destiné à contenir la somme des tf-idf d'un mot
        moyenne=0
        for j in range(1, len(matrice[i]) - 1):
            somme_idf += matrice[i][j]
        moyenne = somme_idf/(len(matrice[i])-1)
        dico_moy_idf[matrice[i][0]]=moyenne
    maxi =0
    liste_mot_important=[]
    for valeur in dico_moy_idf.values():
        if valeur>maxi:
            maxi = valeur
    for cle in dico_moy_idf.keys():
        if dico_moy_idf[cle]==maxi:
            liste_mot_important.append(cle)
    return liste_mot_important

def mots_repetes_chirac(files_names: list):
    # Filtrer les fichiers qui contiennent "Chirac" dans leur nom
    liste_fichier_chirac = [file for file in files_names if "Chirac" in file]

    # Initialiser une liste vide pour stocker les termes fréquents (TF) de chaque fichier
    liste_tf = []

    # Initialiser un dictionnaire pour stocker les termes finaux et leur fréquence totale
    tf_final = {}

    # Parcourir chaque fichier Chirac
    for file in liste_fichier_chirac:
        # Ouvrir le fichier en mode lecture
        with open("cleaned\\" + file, "r", encoding="utf-8") as file:
            # Lire les lignes du fichier et supprimer les caractères de nouvelle ligne
            contenu = file.readlines()
            contenu = [ligne[:-1] for ligne in contenu]

            # Concaténer toutes les lignes en une seule chaîne
            premiere_ligne = ""
            for ligne in contenu:
                premiere_ligne += ligne + (" ")

            # Ajouter les termes fréquents (TF) de la première ligne à la liste
            res=tf_texte(premiere_ligne)
            liste_tf.append(res)

    # Agréger les termes fréquents de chaque fichier dans le dictionnaire tf_final
    for tf1 in liste_tf:
        for mot in tf1:
            if mot not in tf_final:
                tf_final[mot] = tf1[mot]
            else:
                tf_final[mot] += tf1[mot]

    # Trouver la fréquence maximale parmi tous les termes finaux
    maximum = max(tf_final.values())

    # Retourner une liste des termes ayant la fréquence maximale
    return [mot for mot in tf_final if tf_final[mot] == maximum]

def president_nation():
    liste_president= extraction_nom() #extraire les noms des présidents à partir d'une liste de noms de fichiers
    dict_occurence= {president: 0 for president in liste_president}
    presidents_avec_score_positif=[]
    presidents_avec_score_max=[]
    max_score=0

    for i in range(len(liste_president)):
        with open("cleaned\\" +files_names[i], "r", encoding="utf-8") as f:  #le chemin complet du fichier que vous souhaitez ouvrir
            contenu = f.readlines() #Chaque élément de la liste correspond à une ligne du fichier.
            nouveau_contenu = []  # Initialisation d'une nouvelle liste

            for ligne in contenu:
                nouvelle_ligne = ligne[:-1]  # Supprime le dernier caractère de chaque ligne
                nouveau_contenu.append(nouvelle_ligne)  # Ajoute la nouvelle ligne à la liste

            contenu = nouveau_contenu  # Réaffecte la liste modifiée à la variable content
            première_ligne= ""
            for ligne in contenu:
                première_ligne+= ligne + (" ")
            tf = tf_texte(première_ligne)
            if "nation" in tf:
                dict_occurence[liste_president[i]] += tf["nation"] # Ajout du nombre d'occurrences au dictionnaire
            # Liste des présidents pour lesquels le score du mot "nation" est supérieur à zéro :
            presidents_avec_score_positif = []
            for president in dict_occurence:
                if dict_occurence[president] > 0:
                    presidents_avec_score_positif.append(president)

            # Liste des présidents pour lesquels le score du mot "nation" est supérieur à zéro
            presidents_avec_score_positif = [president for president in dict_occurence if
                                              dict_occurence[president] > 0]

            # Liste des présidents dont le score est le plus élevé parmi ceux avec un score positif
            #presidents_avec_score_positif = []
            #max_score = 0  # Initialisation du score maximum à 0
            #boucle qui calcule les score tf maximales
            # parcours des présidents ayant un score tf positif pour "nation"

            for president in presidents_avec_score_positif:
                score = dict_occurence[president]

                # Si le score est supérieur au score maximum actuel
                if score > max_score:
                     presidents_avec_score_max= [president]  # nouvelle liste avec un seul président
                     max_score = score
                # Si le score est égal au score maximum actuel, ajouter le président à la liste
                elif score == max_score:
                    presidents_avec_score_max.append(president) #precision : Si deux ou plusieurs présidents ont le score le plus élevé, ils seront tous ajoutés à la liste


            # Retourne les présidents avec le plus grand score tf pour le mot nation
            return presidents_avec_score_max

def ecologie(directory):
    fichiers = os.listdir(directory)
    liste_present=[]
    for nom in fichiers:
        with open(os.path.join(directory, nom), "r", encoding='utf-8') as fichier:
            texte= fichier.read()
            liste_mot= texte.split()
            for val in liste_mot:
                if val == 'climat' :
                    liste_present.append(nom)
    premier_president=liste_present[0]
    premier_president = premier_president[11:-4]
    return premier_president


if __name__ == '__main__':
    directory = "./speeches"
    files_names = list_of_files(directory, "txt")   #Liste contenant le nom de fichiers texte
    liste_noms = extraction_nom()   #Liste contenant le nom des président
    dico_noms_prenoms = noms_prenoms(liste_noms) #Dictionnaire associant à chaque nom de président son prénom

    if not os.path.exists('cleaned'):  # Vérifie que le dossier 'cleaned' n'existe pas
        os.mkdir('cleaned')  # création du dossier 'cleaned'

    cleaned_dir = './cleaned'
    for nom in files_names:
        nv_fichier = os.path.join(cleaned_dir, nom) #Création d'un nouveau fichier dans le repertoire cleaned
        with open(os.path.join(directory, nom), "r") as speeches, open(nv_fichier, "w") as cleaned_fichier:
            for ligne in speeches:
                nv_ligne = conversion_car(ligne) #Conversion des caracteres spéciaux
                cleaned_fichier.write(nv_ligne)

    print("Bienvenue dans My First ChatBot!",'\n')
    go = 'o' #Cette variable va servir à l'utilisateur de pouvoir tester plusieurs fonctionnalité sans relancer le programme
    while go == 'o':
        print("Que souhaitez vous faire?",'\n')
        print("""
        1.Afficher la liste des mots les moins importants dans le corpus de documents. \n
        2.Afficher le(s) mot(s) ayant le score TF-IDF le plus élevé. \n
        3.Afficher le(s) mot(s) le(s) plus répété(s) par le président Chirac. \n
        4.Afficher le(s) nom(s) du (des) président(s) qui a (ont) parlé de la "Nation" et celui qui l'a répété le plus de fois. \n
        5.Afficher le premier président à parler du climat et/ou de l'écologie \n
        6.Afficher le(s) mot(s) que tous les présidents ont évoqués \n""")

        choix = input("Entrez votre choix:") #Variable nous indiqaunt quelle fonction l'utilisateur souhaite utiliser
        liste_choix=['1','2','3','4','5','6','7'] #Liste des choix possible
        while choix not in liste_choix: #Dans le cas où l'utilisateur rentre une valeur non valide
            print("Attention! Il faut saisir une option existante. Veuillez saisir un nombre entre 1 et 7:")
            choix= input()

        if choix == '1':
            resultat = mot_tf_idf_max('cleaned')
            print("Le(s) mot(s) le(s) plus important dans le corpus de document sont: ")
            for val in resultat:
                print(val, end='\n')
            go = input("Voulez-vous tester une autre fonctionnalité? Taper o pour oui ou n pour non: ")

        elif choix == '2':
            resultat1 = mot_tf_idf_min('cleaned')
            print("Le(s) mot(s) le(s) moins important dans le corpus de document sont: ")
            for val in resultat1:
                print(val, end='\n')
            go = input("Voulez-vous tester une autre fonctionnalité? Taper o pour oui ou n pour non: ")

        elif choix == '3':
            print("Le(s) mot(s) le(s) plus répété(s) par le président Chirac sont:")
            res=mots_repetes_chirac(files_names)
            for val in res:
                print(val)
            go = input("Voulez-vous tester une autre fonctionnalité? Taper o pour oui ou n pour non: ")

        elif choix == '4':
            print("Le(s) nom(s) du (des) président(s) qui a (ont) parlé de la 'Nation' et celui qui l'a répété le plus de fois est:")
            print("Le premier président à parler de climat ou d'écologie est:")
            res=president_nation()
            for val in res:
                print(val)
            go = input("Voulez-vous tester une autre fonctionnalité? Taper o pour oui ou n pour non: ")

        elif choix == '5':
            print("Le premier président à parler de climat ou d'écologie est:")
            print(ecologie('cleaned'))
            go = input("Voulez-vous tester une autre fonctionnalité? Taper o pour oui ou n pour non: ")

        elif choix == '6':
            print("Cette fonctionnalité est encore en cours de développement, merci d'en choisir une autre:")
            go=input()
    print("Vous avez quittez le programme. Merci de votre visite")








        












































