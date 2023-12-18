from formatage_matrice import *
from similarite_calcul import *

def document_pertinent(matriceTFIDF, vecteurTFIDF, liste_nom_fichier):  # utilisé la transposée de la matrice TFIDF
    """Cette fonction prend en paramètre le matrice TF_IDF du corpus, le vecteur-TF_IDF de la question et la liste
    des noms de fichiers du répertoire étudié et renvoie le document le plus pertinent pouvant nous aider à répondre à
    la question """
    max = 0
    doc = 0
    matrice= vrai_t(matriceTFIDF) # matrice est transposee "nettoyé" de la matriceTFIDF (on enlève la 1er sous liste et le premier mot de chaque sous liste)
    for i in range(0, len(matrice)):
        res = similarite(matrice[i], vecteurTFIDF) # Pour chaque liste de la matrice on calcul la similarite de celle ci avec le vecteur de la question
        if res > max:
            max = res
            doc = i # La position du doc dans la liste doc sera alors égale à i
    return liste_nom_fichier[doc]







        












































