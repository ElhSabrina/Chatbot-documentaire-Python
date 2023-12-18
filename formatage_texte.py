import os

def liste_fichier(repertoire, extension):
    """Cette fonction prend en paramétre un répertoire et une extension (txt dans notre cas) et renvoie
     le nom de tous les fichiers du répertoire sous la forme d'une liste"""
    noms_fichiers = []
    for nom_fichier in os.listdir(repertoire):
        if nom_fichier.endswith(extension):
            noms_fichiers.append(nom_fichier)
    return noms_fichiers

def extraction_nom():
    """Cette fonction renvoie la liste des noms des présidents dont leurs discourt et contenu dans le dossier speeches"""
    noms=""
    repertoire = "./speeches"
    liste_noms_fichiers = liste_fichier(repertoire, "txt")
    liste_noms=[]
    for i in range(len(liste_noms_fichiers)): # On parcourt la liste des noms des fichiers
        noms=liste_noms_fichiers[i]
        noms=noms[11:-4] # On effectue un slice pour se débarasser de "Nomination_" et de ".txt"
        if noms[-1] == '1' or noms[-1]=='2': # Certain président ont un 1 ou un 2 collé à leurs prénom
            noms=noms[:-1]
        liste_noms.append(noms) # On ajoute le nom à la liste liste_noms
    return liste_noms

def noms_prenoms(liste_noms):
    """Cette fonction prend en paramètre une liste de noms et renvoie un dictionnaire associant à chaque nom (clé)
    son prénom (valeur)"""
    dictionnaire_presidents={}
    for nom in liste_noms: # Pour chaque nom de la liste_noms
        if nom == 'Macron': # On associe chaque nom à soon prénom
            dictionnaire_presidents[nom]='Emmanuel'
        elif nom == 'Sarkozy':
            dictionnaire_presidents[nom]='Nicolas'
        elif nom == 'Chirac':
            dictionnaire_presidents[nom]='Jacques'
        elif nom =='Giscard dEstaing':
            dictionnaire_presidents[nom]='Valérie'
        elif nom =='Hollande'or nom=='Mitterand': # Ici deux présidents on le même prénom
            dictionnaire_presidents[nom]='François'
    return dictionnaire_presidents

def conversion_car(texte):
    """Cette fonction permet de convertir un texte en minuscule et d'enlever les caractères spéciaux"""
    nv_texte="" # Variable allant contenir le nouveau texte formater
    liste_caractere=[',','.',':','?',';','!','-',"'","&",chr(34)] # Liste contenant les caractères spéciaux à retirer
    for caractere in texte:
        if 'A' <= caractere <= 'Z':
            nv_texte += chr(ord(caractere)+32) # On ajoute au nv_texte son équivalent en minuscule
        elif caractere in liste_caractere:
            nv_texte += ' ' # On le remplace par un espace qu'on ajoute à la variable nv_texte
        else:
            nv_texte += caractere # Dans les autres cas on ajoute le caractère à la chainede caractère nv_texte
    return nv_texte

