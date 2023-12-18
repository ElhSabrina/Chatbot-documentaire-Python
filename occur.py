def occur(chaine):
    """Cette fonction prend en paramètre une chaine de caractère est renvoie l'occurence de chaque mot de la chaine de
    la chaine de caractère"""
    liste_mot =chaine.split() # Liste contenant tous les mots de la chaine de caractère chaine
    dico_occur= {}
    for val in liste_mot:
        if val not in dico_occur.keys(): # Si le mot n'est pas encore en clé du dictionnaire dico_occur
            dico_occur[val]=1 # On associe à la clé val donc au mot une occurrence de 1
        else:
            dico_occur[val] += 1 # Si val est déja une clé dans le dictionnaire on incrémente sa valeur de 1
    return dico_occur
