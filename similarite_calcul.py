from math import *

def produit_scalaire(A, B):

    produit_scalaire_resultat = 0
    for i in range(len(A)):
        produit_scalaire_resultat += A[i] * B[i]
    return produit_scalaire_resultat

def norme_vecteur(A):
    norme = 0
    for i in range(len(A)):
        norme += A[i] ** 2
    norme = sqrt(norme)
    return norme

def similarite(A, B):
    """Calcul de la similarité prend en parametre la matrice transposée nettoyé de i et le vecteur de la question
    et renvoie la similarité """
    produit_scalaire_resultat = produit_scalaire(A, B)
    norme_A = norme_vecteur(A)
    norme_B = norme_vecteur(B)

    if norme_A == 0 or norme_B == 0:
         return 0

    similarite = produit_scalaire_resultat / (norme_A * norme_B)
    return similarite


