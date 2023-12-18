from matrice_tf_idf import *
def vrai_t(matrice):
    """Cette fonction prend en paramètre une matrice transposée et renvoie la matrice sans la première sous liste et
    enlève le première élement de toutes le autres sous listes """
    nouvelle_matrice = [ligne[1:] for ligne in matrice[1:]]
    return(transposee(nouvelle_matrice))

def vrai(matrice):
    """Cette fonction prend en paramètre une matrice et la renvoie sans la première sous liste et
    enlève le première élement de toutes le autres sous listes """
    nouvelle_matrice = [ligne[1:] for ligne in matrice[1:]]
    return (nouvelle_matrice)
