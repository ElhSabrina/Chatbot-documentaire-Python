def tokenisation(question):
    """Cette fonction prend en paramètre une chaine de caractère et renvoie une liste contenant les mots de la
    question en majuscule et sans caractère spécail sous forme de liste"""
    question_formater = conversion_car(question) # On convertit les majuscules en minuscules et on supprime les caractères spéciaux
    liste_mots = question_formater.split() # On met les mots de la nouvelle chaine de caractères dans la liste_mots
    return liste_mots


def recherche_mot_question(liste, directory):
    """Cette fonction prend en paramètre une liste et un repertoire et renvoie une liste des termes présents à la fois
     dans la liste est dans les fichiers du répértoires directory"""
    fichiers = os.listdir(directory)
    contenu_global = []
    liste_mot_commun = []
    for nom in fichiers: # On parcourt les fichiers un par un
        with open(os.path.join(directory, nom), "r",encoding='utf-8') as fichier:
            texte = fichier.read()
            list_texte = texte.split() # La liste_texte contient tous les mots du fichier
        contenu_global += list_texte # On ajoute chaque liste à une liste

    for i in range(len(liste)): # On parcourt chaque mot de la liste en parametre
        if liste[i] in contenu_global:
            liste_mot_commun.append(liste[i]) # Si le mot est dans le contenu global on l'ajoute à la liste des mots communs
    return liste_mot_commun
