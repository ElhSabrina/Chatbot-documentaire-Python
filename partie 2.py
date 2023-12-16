from fonction_de_base import*
def tokenisation(question):
    question_formater = conversion_car(question)
    liste_mots = question_formater.split()
    return liste_mots

def recherche_mot_question(liste,directory):
    fichiers = os.listdir(directory)
    contenu_global=[]
    liste2=[]
    for nom in fichiers:
        with open(os.path.join(directory, nom), "r",encoding='utf-8') as fichier:  # On effectue un parcourt de chaque fichier un par un
            texte = fichier.read()  # la variable texte contient le contenu du fichier parcouru
            list_texte = texte.split()
        contenu_global += list_texte
    for mot in liste:
        if mot in contenu_global:
            liste2.append(mot)
    return liste2

def vrai_t(matrice):
    nouvelle_matrice = [ligne[1:] for ligne in matrice[1:]]
    return(transposee(nouvelle_matrice))

def vrai(matrice):
    nouvelle_matrice = [ligne[1:] for ligne in matrice[1:]]
    return (nouvelle_matrice)

def calcul_vecteur_tf_idf(question,matrice): #renvoie le vecteur sous forme de liste
    dico_idf = idf('cleaned')
    dico_tf = tf_texte(question)
    vecteur_question=[]
    liste_question= question.split()
    for i in range(1,len(matrice)):
        if matrice[i][0] in liste_question:
            tfidf=dico_tf[matrice[i][0]]*dico_idf[matrice[i][0]]
        else:
            tfidf= 0.0
        vecteur_question.append(tfidf)
    return vecteur_question

def calcul_vecteur_tf_idf2(question,matrice): #renvoie le vecteur sous forme de dictionnaire UTILISER LA MATRICE TFIDF DU CORPUS
    dico_idf = idf('cleaned')
    dico_tf = tf_texte(question)
    vecteur_question={}
    liste_question = question.split()
    for i in range(1,len(matrice)):
        if matrice[i][0] in liste_question:
            vecteur_question[matrice[i][0]]=dico_tf[matrice[i][0]]*dico_idf[matrice[i][0]]
        else:
            vecteur_question[matrice[i][0]]=0.0
    return vecteur_question


def produit_scalaire(A, B):
    while len(A) != len(B):
        A = []
        input_A = input("Entrez la liste A séparée par des espaces : ")
        for element in input_A.split():
            A.append(float(element))

        B = []
        input_B = input("Entrez la liste B séparée par des espaces : ")
        for element in input_B.split():
            B.append(float(element))

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
    produit_scalaire_resultat = produit_scalaire(A, B)
    norme_A = norme_vecteur(A)
    norme_B = norme_vecteur(B)

    if norme_A == 0 or norme_B == 0:
         return 0

    similarite = produit_scalaire_resultat / (norme_A * norme_B)
    return similarite


def mots_tf_idf_eleves(question):
    vecteur_tf_idf = calcul_vecteur_tf_idf(question)
    maxi = 0
    mots_max = []

    for cle, elem in vecteur_tf_idf.items():
        if elem > maxi:
            maxi = elem
            mots_max = [cle]
        elif elem == maxi:
            mots_max.append(cle)

    return mots_max
#test
print(calcul_vecteur_tf_idf(""))
print(produit_scalaire([1,2],[3,4]))
print(norme_vecteur([1,2,3]))
print(similarite([1,2,3],[3,4,5]))
print(mots_tf_idf_eleves("hi guys je la ecologie suis sabrina"))

def extraire_premiere_phrase_max_tf_idf(question):
    doc = doc_pertinent(question)
    mots_max_tf_idf = mots_tf_idf_eleves(question)

    # Parcourir le document pour extraire la première phrase contenant l'un des mots
    with open(f"cleaned/{doc}", "r", encoding='utf-8') as file:
        for line in file:
            phrases = line.split('.')
            for phrase in phrases:
                for mot in mots_max_tf_idf:
                    if mot in phrase:
                        premiere_phrase_trouvee = phrase.strip()
                        break  #des qu'un premier mot est trouvé on stop la boucle
                if premiere_phrase_trouvee:
                    break  #des que la phrase est trouvée on stop l'autre boucle aussi

    return premiere_phrase_trouvee

def sous_chaine(str1, str2):
    token_str1 = tokenisation(str1)
    token_str2 = tokenisation(str2)
    for elem in token_str1:
        if elem not in token_str2:
            return False
    return True
    
def document_pertinent(matriceTFIDF,vecteurTFIDF,liste_nom_fichier):#utilisé la transposée de la matrice TFIDF
    max=0
    doc=0
    for i in range(1,len(matriceTFIDF)):
        matrice1= matriceTFIDF[i][1:]
        print(len(matrice1),len(vecteurTFIDF))
        res= similarite(matrice1,vecteurTFIDF)
        if res>max:
            max = res
            doc=i-1
    return liste_nom_fichier[doc]
    
def ameliorer_reponse(question):
    question = tokenisation(question)
    premiere_phrase_trouvee = extraire_premiere_phrase_max_tf_idf(question)

    question_starters = {
        "Comment": "Après analyse, ",
        "Pourquoi": "Car, ",
        "Peux-tu": "Oui, bien sûr!"

    }
    mot_cle = question[0]
    for elem in question_starters.keys():
        if sous_chaine(mot_cle, elem) or sous_chaine(elem, mot_cle):
            premiere_phrase_trouvee = question_starters[elem] + premiere_phrase_trouvee
            break #dés qu'il y a une clé qui correspond au premier mot du dico on stoppe la boucle

    return premiere_phrase_trouvee
