from mot_tfidf_min_max import *
from recherche_textuelle import *
from generation_rep import *
import os


if __name__ == '__main__':

    directory = "./speeches"
    files_names = list_of_files(directory, "txt")   #Liste contenant le nom de fichiers texte
    liste_noms = extraction_nom()   #Liste contenant le nom des président
    dico_noms_prenoms = noms_prenoms(liste_noms) #Dictionnaire associant à chaque nom de président son prénom

    if not os.path.exists('cleaned'):  # Vérifie que le dossier 'cleaned' n'existe pas
        os.mkdir('cleaned')  # création du dossier 'cleaned'

    cleaned_dir = './cleaned'
    for nom in files_names:
        nv_fichier = os.path.join(cleaned_dir, nom) #Création d'un nouveau fichier dans le repertoire cleaned
        with open(os.path.join(directory, nom), "r") as speeches, open(nv_fichier, "w") as cleaned_fichier:
            for ligne in speeches:
                nv_ligne = conversion_car(ligne) #Conversion des caracteres spéciaux
                cleaned_fichier.write(nv_ligne)

    print("Bienvenue dans My First ChatBot!",'\n')
    go = 'o' #Cette variable va servir à l'utilisateur de pouvoir tester plusieurs fonctionnalité sans relancer le programme
    while go == 'o':
        print("Que souhaitez vous faire?",'\n')
        print("Accèder à ChatBot 1. Tapez 1",'\n')
        print("Accèder à Chatbot 2. Tapez 2",'\n')
        choix1 = input("Entrez votre choix:")
        liste_choix1=['1','2']
        while choix1 not in liste_choix1:
            print("Attention! Il faut saisir une option existante. Veuillez saisir un chiffre entre 1 et 2")
            choix1=input()
        if choix1 == '1':
            print("Vous êtes actuellement dans My First Chat Bot 1",'\n')
            print("Que souhaitez vous faire")
            print("""
            1.Afficher la liste des mots les moins importants dans le corpus de documents. \n
            2.Afficher le(s) mot(s) ayant le score TF-IDF le plus élevé. \n
            3.Afficher le(s) mot(s) le(s) plus répété(s) par le président Chirac. \n
            4.Afficher le(s) nom(s) du (des) président(s) qui a (ont) parlé de la "Nation" et celui qui l'a répété le plus de fois. \n
            5.Afficher le premier président à parler du climat et/ou de l'écologie \n""")
            choix2 = input("Entrez votre choix:") #Variable nous indiqaunt quelle fonction l'utilisateur souhaite utiliser
            liste_choix2 =['1','2','3','4','5'] #Liste des choix possible
            while choix2 not in liste_choix2: #Dans le cas où l'utilisateur rentre une valeur non valide
                print("Attention! Il faut saisir une option existante. Veuillez saisir un nombre entre 1 et 7:")
                choix= input()
            if choix2 == '1':
                resultat1 = mot_tf_idf_min('cleaned')
                print("Le(s) mot(s) le(s) moins important dans le corpus de document sont: ")
                for val in resultat1:
                    print(val, end='\n')
                go = input("Voulez-vous tester une autre fonctionnalité? Taper o pour oui ou n pour non: ")

            elif choix2 == '2':
                resultat = mot_tf_idf_max('cleaned')
                print("Le(s) mot(s) le(s) plus important dans le corpus de document sont: ")
                for val in resultat:
                    print(val, end='\n')
                go = input("Voulez-vous tester une autre fonctionnalité? Taper o pour oui ou n pour non: ")


            elif choix2 == '3':
                print("Le(s) mot(s) le(s) plus répété(s) par le président Chirac sont:")
                res=mots_repetes_chirac(files_names)
                for val in res:
                    print(val)
                go = input("Voulez-vous tester une autre fonctionnalité? Taper o pour oui ou n pour non: ")

            elif choix2 == '4':
                print("Le(s) nom(s) du (des) président(s) qui a (ont) parlé de la 'Nation' et celui qui l'a répété le plus de fois est:")
                print("Le premier président à parler de climat ou d'écologie est:")
                res=president_nation()
                for val in res:
                    print(val)
                go = input("Voulez-vous tester une autre fonctionnalité? Taper o pour oui ou n pour non: ")

            elif choix2 == '5':
                print("Le premier président à parler de climat ou d'écologie est:")
                print(ecologie('cleaned'))
                go = input("Voulez-vous tester une autre fonctionnalité? Taper o pour oui ou n pour non: ")
        if choix1 == '2':
            print("Vous êtes actuellement dans My First Chat Bot 2",'\n')
            question = input("Saisissez une question:")
            print(ameliorer_reponse(question))
            go = input("Voulez-vous tester une autre fonctionnalité? Taper o pour oui ou n pour non: ")


    print("Vous avez quittez le programme. Merci de votre visite")






        












































