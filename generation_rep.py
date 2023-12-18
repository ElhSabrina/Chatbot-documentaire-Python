from matrice_tf_idf import *
from vecteur_tf_idf import *
from tokenisation import *
from document_pertinent import *
from formatage_texte import *
def mots_tf_idf_eleves(question):
    matrice= matrice_tf_idf('cleaned')
    vecteur_tf_idf = calcul_vecteur_tf_idf(question,matrice)
    maxi = 0
    compteur=0
    for i in range(len(vecteur_tf_idf)):
        if vecteur_tf_idf[i]>maxi:
            maxi = vecteur_tf_idf[i]
            compteur = i
    eleve = matrice[compteur+1][0]
    return eleve

def sous_chaine(str1, str2):
    token_str1 = tokenisation(str1)
    token_str2 = tokenisation(str2)
    for elem in token_str1:
        if elem not in token_str2:
            return False
    return True

def extraire_premiere_phrase_max_tf_idf(question):
    matrice_cleaned = matrice_tf_idf('cleaned')
    vecteur_question = calcul_vecteur_tf_idf(question, matrice_cleaned)
    doc = document_pertinent(matrice_cleaned,vecteur_question,list_of_files('cleaned',"txt"))
    mots_max_tf_idf = mots_tf_idf_eleves(question)
    premiere_phrase_trouvee = None
    phrases=[]
    liste_phrase_trouvee=[]
    contenu_brut =""
    mot_virgule = mots_max_tf_idf +"," # Stock le mot pertinent suivie d'une virgule
    mot_point = mots_max_tf_idf +"." # Stock le mot petinent suivie d'un point
    mot_maj = chr(ord(mots_max_tf_idf[0])-32)+mots_max_tf_idf[1:] # Stock le mot petinent commencant par une majuscule

    with open(f"speeches/{doc}", "r", encoding='utf-8') as file: #On ouvre le document pertinent
        contenu = file.read()
        for car in contenu:
            if car != '\n' and car != "\"": # Si ce n'est pas un saut de ligne ou un slash
                contenu_brut += car
        phrases=contenu_brut.split('.') #On note que si la phrase se termine par ? on prendra la fin de la phrase suivante
        for phrase in phrases:
            liste_mot= phrase.split()
            for mot in liste_mot:
                if mot == mots_max_tf_idf or mot == mot_point or mot == mot_virgule or mot == mot_maj:#Si le mot sans une de ses quatres formes est dans liste de mot
                    liste_phrase_trouvee.append(phrase)
    if liste_phrase_trouvee == []:
        # Si la liste est vide cela signifie que le mot avec le tf_idf le plus élevé dans la question n'est pas présent dans le document avec laquelle elle a la plus grande similarité
        # Sans l'instruction suivante on obtiendrait un Index Error
        premiere_phrase_trouvee = "Nous ne sommes pas encore en capacité de vous fournir une réponse" #
    else:
        premiere_phrase_trouvee = liste_phrase_trouvee[0] # On prend le première élément de la liste car il se peut qu'elle contienne plusieurs phrase
    return premiere_phrase_trouvee

def ameliorer_reponse(question):
    question1 = tokenisation(question)
    vecteur_tf_idf = calcul_vecteur_tf_idf(question,matrice=matrice_tf_idf('cleaned'))
    premiere_phrase_trouvee = extraire_premiere_phrase_max_tf_idf(question)

    question_starters = {
        "Comment": "Après analyse, ",
        "Pourquoi": "Car, ",
        "Peux-tu": "Oui, bien sûr!"

    }
    mot_cle = question1[0]
    for elem in question_starters.keys():
        if sous_chaine(mot_cle, elem) or sous_chaine(elem, mot_cle):
            premiere_phrase_trouvee = question_starters[elem] + premiere_phrase_trouvee
            break  # dés qu'il y a une clé qui correspond au premier mot du dico on stoppe la boucle

    return premiere_phrase_trouvee

