from matrice_tf_idf import *


def mot_tf_idf_min(repertoire):
    """Cette fonction prend en paramètre un répertoire et renvoie les mots ayant le TF_IDF le plus petit"""
    matrice = matrice_tf_idf(repertoire) # Matrice contenant le tf-idf du repertoire
    dico_moy_idf = {}
    liste_mot=[]
    for i in range(1, len(matrice)): # On parcourt les sous listes de la matrice à partir de la deuxième (la première contient les noms)
        somme_idf = 0
        moyenne=0
        for j in range(1, len(matrice[i])):
            somme_idf += matrice[i][j]
        moyenne = somme_idf/(len(matrice[i])-1) # On calcul la moyenne
        dico_moy_idf[matrice[i][0]]=moyenne # On associe à chaque mot la moyenne de ses TF-IDF

    mini = 1 # On initialise mini à 1 car la moyenne des TF-IDF sera forcement inférieur à 1
    liste_mot_moins_important=[]
    for valeur in dico_moy_idf.values(): # On parcourt les valeurs du dictionnaire contenant la moyenne des TF-ODF
        if valeur<mini:
            mini = valeur

    for cle in dico_moy_idf.keys(): #Pour chaque clé du dictionnaire contenant les moyennes de TF-IDF
        if dico_moy_idf[cle]==mini: #Si la valeur du du mot (de la clé) est égale à la variable mini
            liste_mot_moins_important.append(cle)
    return liste_mot_moins_important


def mot_tf_idf_max(repertoire):
    """Cette fonction prend en paramètre un répertoire et renvoie le(s) mot(s) ayant le score TF-IDF le plus important.
    Il se base sur le même pricipe que la fonction précdente en faisant la moyenne des scores TF-IDF de chaque mot
    et renvoie le(s) mot(s) ayant la moyenne la plus élevé."""
    matrice = matrice_tf_idf(repertoire)# Matrice contenant le tf-idf dur repertoire
    dico_moy_idf = {}
    liste_mot=[]
    for i in range(1, len(matrice)):
        somme_idf = 0 # création d'une fonction destiné à contenir la somme des tf-idf d'un mot
        moyenne=0
        for j in range(1, len(matrice[i])):
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
