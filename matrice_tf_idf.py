from idf import *
from tf import *
from formatage_texte import *
def transposee(matrice):
    result_matrix = []

    for col in range(len(matrice[0])):
        line_matrix = []
        for line in range(len(matrice)):
            line_matrix.append(matrice[line][col])
        result_matrix.append(line_matrix)

    return result_matrix

def matrice_tf_idf(directory):
    """Cette fonction prend en paramètre un répertoire et renvoie la matrice TF-IDF de corpus sous la forme de
    liste de liste"""
    matrice = []  # Initialisation de la matrice TF-IDF
    mots_uniques = list(idf(directory).keys())  # Liste de tous les mots uniques de tous les fichiers
    ligne_1 = ["Les mots: "]
    for mot in mots_uniques:
        ligne_1.append(mot)  # liste de tous les mots uniques de tous les fichiers
    matrice.append(ligne_1)  # on ajoute une première liste dans la matrice avec tous les mots
    score_idf = idf(directory)  # on affecte le score idf de tous les mots du répertoire dans un dictionnaire

    for file in list_of_files(directory,extension="txt"):
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
