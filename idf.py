import os
from math import *

def idf(repertoire):
    """Cette fonction prend en paramètre un répertoire de fichier et renvoie le dictionnaire associant à chaque mot
    son idf"""
    fichiers= os.listdir(repertoire)
    dico_idf ={}
    liste_texte=[]
    liste_texte2=[]
    nb=len(fichiers)
    for nom in fichiers: # Parcourt fichier par fichier
        with open(os.path.join(repertoire, nom), "r", encoding='utf-8') as fichier: # On ouvre le fichier en mode lecture
            contenu = fichier.read()
            liste_mot = contenu.split() # Liste contenant tous les mots du texte
        liste_texte.append(liste_mot) # Liste contenant toutes les liste_mot

    for liste in liste_texte:
        nvliste=[]
        for val in liste:
            if val not in nvliste: # Si val (le mot) n'est pas dans la nvliste
                nvliste.append(val) # On l'ajoute à la liste nvliste
                # On note qu'ici on n'utilise pas un set pour garder le bonne ordre
        liste_texte2.append(nvliste)

    #Ici on compte combien de fois chaque mot apparait dans tout le corpus
    for liste in liste_texte2:
        for mot in liste:
            if mot not in dico_idf.keys(): # Si le mot n'est pas en clé du dictionnaire dico_idf
                dico_idf[mot] = 1 #On crée une paire clé/valeur avec comme clé le mot et en valeur 1
            else:
                dico_idf[mot]+=1 # On incrément la valeur de la clé de 1
    for cle, valeur in dico_idf.items():
        dico_idf[cle]=log((nb/valeur), 10) # On associe à chaque clé (mot) son idf
    return dico_idf
