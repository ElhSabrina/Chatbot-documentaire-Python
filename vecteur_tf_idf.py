from tf import *
from idf import *
from formatage_texte import *
from tokenisation import *
def calcul_vecteur_tf_idf(question,matrice): #renvoie le vecteur sous forme de liste 
    """Cette fonction prend en paramètre la question et la matriceTFIDF du répertoire et renvoie le vecteur TF_IDF
    de la question sous forme de liste. On note que l'ordre des TF_IDF correspond à l'ordre de ceux de la matrice"""
    dico_idf = idf('cleaned') # Dictionnaire contenant l'IDF des mots du répetoire cleaned
    dico_tf = tf_texte(conversion_car(question)) # Dictionnaire contenant le TF des mots de la question convertie en minuscule et sans caractère spéciaux
    vecteur_question=[]
    liste_question= tokenisation(question) # Liste contenant tous les mots de la question (en minuscule)
    for i in range(1,len(matrice)):
        if matrice[i][0] in liste_question: # Si le premier terme de la sous liste de la matrice soit le mot est dans la liste de mot de la question
            tfidf= dico_tf[matrice[i][0]]*dico_idf[matrice[i][0]] # La variable tfidf prend la valeur du du tf du mot dans la question multiplié par le idf du mot dans le corpus
        else:
            tfidf= 0.0 # Sinon la variable prend la valeur 0.0
        vecteur_question.append(tfidf) # On ajoute la valeur de la variable tfidf au vecteur de la question
    return vecteur_question
