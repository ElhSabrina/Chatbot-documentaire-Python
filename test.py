from math import

def occur(chaine):
    liste_mot=chaine.split()
    liste_compteur=[]
    liste_test=[]
    i=0
    while liste_mot[i] not in liste_test and i<=len(liste_mot):
        liste_test.append(liste_mot[i])
        compteur=0
        for j in liste_mot:
            if liste_mot[i]==j:
                compteur+=1
        liste_compteur.append(compteur)
        i+= 1
    dico= dict(zip(liste_mot,liste_compteur))
    return(dico)
print(occur("bonjour je m appelle bonjour"))

def IDF(repertoire):
    for mot in dico:

        def calculer_transposee(matrice):
            # Fonction pour calculer la transposée d'une matrice
            nombre_lignes = len(matrice)
            nombre_colonnes = 0

            if nombre_lignes > 0:
                nombre_colonnes = len(matrice[0])

            transposee = []

            for j in range(nombre_colonnes):
                ligne_transposee = []
                for i in range(nombre_lignes):
                    ligne_transposee.append(matrice[i][j])
                transposee.append(ligne_transposee)

            return transposee






