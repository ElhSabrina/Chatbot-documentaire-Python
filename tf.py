from occur import *

def tf(fichier):
    """Cette fonction prend en parmètre un fichier et renvoie un dictionnaire associant à chaque mot son score TF. On
    admet que le score TF d'un mot est le quotient de son occurence sur le nombre de mot du fichier"""
    with open(fichier,"r", encoding = 'utf-8') as f: # On ouvre le fichier en mode lecture
        texte = f.read() # La variable texte est une chaine de caractère contenat le contenu du fichier f
        nb_mots = len(texte.split())
        dico_occur = occur(texte) # Ce dictionnaire associe à chaque mot son occurence dans le texte
        for cle, valeur in dico_occur.items():
            dico_occur[cle] = valeur/nb_mots # On associe à chaque mot (clé) son TF (valeur)
    return dico_occur

def tf_texte(texte):
    """Cette fonction prend en paramètre un texte et renvoie un dictionnaire associant à chauqe mot son TF.
    Cette fonction se base sur le même pricipe que la présente mais nous permet d'avoir le tf d'une chaine
    de caractère qui ne se trouve pas dans un fichier."""
    nb_mots=len(texte.split())
    dico_occur = occur(texte)
    for cle, valeur in dico_occur.items():
        dico_occur[cle]= valeur/nb_mots
    return dico_occu
