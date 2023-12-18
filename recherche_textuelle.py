from tf import *
from formatage_texte import *
import os

def mots_repetes_chirac(liste_noms_fichiers: list):
    """Cette fonction prend en paramètre une liste de fichier est renvoie le(s) mot(s) le(s) plus répété(s) par
    le président Jacques Chirac"""
    liste_fichier_chirac = [fichier for fichier in liste_noms_fichiers if "Chirac" in fichier]# Filtrer les fichiers qui contiennent "Chirac" dans leur nom

    # Initialiser une liste vide pour stocker les termes fréquents (TF) de chaque fichier
    liste_tf = []

    # Initialiser un dictionnaire pour stocker les termes finaux et leur fréquence totale
    tf_final = {}

    # Parcourir chaque fichier Chirac
    for fichier in liste_fichier_chirac:
        # Ouvrir le fichier en mode lecture
        with open("cleaned\\" + fichier, "r", encoding="utf-8") as fichier:
            # Lire les lignes du fichier et supprimer les caractères de nouvelle ligne
            contenu = fichier.readlines()
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
    """Cette fonction renvoie le nom du président ayant le plus parler de la nation"""
    liste_president= extraction_nom() #extraire les noms des présidents à partir d'une liste de noms de fichiers
    dict_occurence= {president: 0 for president in liste_president}
    presidents_avec_score_positif=[]
    presidents_avec_score_max=[]
    max_score=0
    fichiers_noms = liste_fichier('cleaned',"txt")
    for i in range(len(liste_president)):
        with open("cleaned\\" +fichiers_noms[i], "r", encoding="utf-8") as f:  #le chemin complet du fichier que vous souhaitez ouvrir
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


def ecologie(repertoire):
    """Cette fonction prend en paramètre un répertoire de fichier texte et renvoie le nom du premier président ayant
    parler du climat ou de l'écologie"""
    fichiers = os.listdir(repertoire) # Contient la liste des noms des fichiers du répertoire
    liste_present=[]
    for nom in fichiers:
        with open(os.path.join(repertoire, nom), "r", encoding='utf-8') as fichier :
            texte= fichier.read()
            liste_mot= texte.split() # Liste contenant tous les mots de la variable texte
            for val in liste_mot:
                if val == 'climat'  : # Si val (le mot) est égale à climat ou ecologie
                    liste_present.append(nom) # On ajoute le nom du fichier à la liste
    premier_president=liste_present[0] # Le premier fichier où on parle de climat où d'écologie et le premier de la liste
    premier_president = premier_president[11:-4] # On extrait le nom du président
    return premier_president

