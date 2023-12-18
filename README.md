groupe A, Sabrina El hassani/ Lucy Gros
My First Chat Bot est un projet ayant pour but d'analyser des fichiers texte d'un répertoire.
L'analyse effectué est à plusieurs niveau allant de la recherche automatique à la génération d'
une réponse à la question d'un utlisateur.

Le projet est actuellement terminé bien qu'il pourrait bénéficier de plusieurs amélioration
notamment dans la gestion de cas ou bien dans l'interface utilisateur.

Voici toutes les fonctions utilisées dans notre projet ainsi que leur utilisation:

list_of_files(directory,extension) : "directory" est le nom du répertoire où se trouve
les fichiers textes de départ, "extension" est le type d'extension des fichiers contenu
dans le répertoire lorqu'on appelle la fonction on peut mettre l'extension "txt".
La fonction retourne la liste des fichiers du répertoir directory.
Ainsi dans notre cas on peut appeler notre fonction en faisant:
list_of_files("cleaned","txt")

extraction_nom() : La fonction ne prend rien en paramètre car elle extrait des noms des fichiers
d'un répertoir prédéfinit soit le répertoire speeches.
La fonction retourne la liste des noms de de chaque président.
Ainsi on peut appeler notre fonction en faisant:
extraction_nom()

nom_prenoms(liste_noms): La fonction prend en paramètre une liste de noms. Donc une
liste de chaine de caractère. Elle retourne un dictionnaire associant à chaque nom d'un
président son prénom. Si la fonction extraction nom nous permet d'avoir la liste des noms
de présidents on peut donc appeler la fonction en faisant:
liste_nom = extraction_nom()
nom_prenom(liste_nom)

conversion_car(texte): La fonction prend en paramètre une chaîne de caractère texte et renvoie une
autre chaine de caractère convertit (sans majuscule et caractères spéciaux)

occur(chaine): La fonction prend en paramètre une chaine de caractère et renvoie l'occurence de chaque
mot de la chaine de caractère sous la forme d'un dictionnaire ayant pour les clé le mot et comme valeur
son occurrence.

tf(fichier): La fonction prend en paramètre un fichier texte et renvoie un dictionnaire associant à chaque
mot de se fichier son TF.
Ainsi on peut l'appeler en faisant:
tf("Nomination_Macron")

tf_texte(texte): La fonction prend en paramètre une chaine de caractère et renvoie un dictionnaire associant
à chaque mot (clé) son Tf (valeur).

idf(directory): Cette fonction prend en paramètre un répetoire ici se sera toujours un réperoire
cleaned et retourne un dictionnaire associant à chaque mot son score IDF.
On peut l'appeler en faisant:
idf('cleaned')

transposee(matrice) : Cette fonction prend en paramètre une matrice soit liste 2D et renvoie la
transposée de cette matrice donc une autre liste2D.

matrice_tf_idf(directory): Cette fonction prend en paramètre un répertoire de type cleaned (formater)
et retourne une liste 2D correspond à la matrice TF_IDF du corpus.
On peut l'appeler en faisant:
matrice_tf_idf('cleaned')

mot_tf_idf_min(directory) : Cette fontion prend en paramètre un répertoire du type cleaned et retourne une liste contenant
les mots ayant le tf_idf le moins élevé.
On peut l'appeler en faisant :
mot_tf_idf_min('cleaned')

mot_tf_idf_max(directory): Cette fontion prend en paramètre un répertoire du type cleaned et retourne une liste contenant
les mots ayant le tf_idf le plus élevé.
On peut l'appeler en faisant:
mot_tf_idf_max('cleaned')

mots_repetes_chirac(files_names) : Cette fonction prend en paramètre une liste de noms de fichiers texte et retourne
une liste de chaine de caractère.
On peut l'appeler en faisant:
mots_repetes_chirac(list_of_files('cleaned')

president_nation(): ne prend rien en paramètre et renvoie une liste;

ecologie(directory): Cette fontion prend en paramètre un répertoire du type cleaned et retourne une chaine de caractère
contenant le nom du premier président à parler d'écologie.
On peut l'appeler en faisant :
ecologie('cleaned')

vrai_t(matrice):prend en paramètre la matrice TF-IDF (liste 2D) du corpus et renvoie la transposée (liste 2D) sans les
informations textuelle cette à dire sans la première sous liste contenant tous les mots ni le premier mot de chaque sous listes
correspondant à une chaine de caractère.
On peut l'appeler en faisant:
vrai_t(matrice_tf_idf('cleaned'))

vrai(matrice) : prend en paramètre la matrice TF_IDF (liste 2D) du corpus et renvoie celle si sans la premières sous
listes correspondant aux noms des documents  et sans le premier mot de chaque sous liste correspondant  à une chaine de
caractère.

tokenisation(question): Cette fonctin prend en paramètre une chaine de caractère et renvoie une liste de chaine de
caractère correspond à la liste des mots de la chaine de caratère mise en paramètre;
On peut l'appeler en faisant:
tokenisation("Fait-il beau aujourd'hui?")

recherche_mot_question(liste,directory): Cette fonction prend en paramètre une liste correspondant à la liste de mot d'une
chaine de caractère et un répertoire du type cleaned. Elle renvoie une liste correspondant à la liste des mots en commun
entre un phrase tokénisé et un répertoire de fichier texte.
On peut l'utiliser en faisant:
recherche_mot_question(tokenisation("Fait-il beau aujourd'hui"), 'cleaned')

calcul_vecteur_tf_idf(question,matrice): prend en paraamètre une chaine de caractère correspondant à la matrice TF-IDF
du corpus et renvoie une liste correspondant au vecteur tf-IDF de la question.
On peut l'appeler en faisant :
calcul_vecteur_tf_idf("Fait-il beau aujourd'hui?",matrice_tf_if('cleaned'))

produit_scalaire(A, B): prend en paramètre deux liste de réel dans notre cas et renvoie un réel correspondant au
produit scalaire de ces deux liste.

norme_vecteur(A): prend en paramètre une liste de réel et renvoie un réel correpondant à la norme de ce vecteur (liste)

similarite(A,B) : prend en paramètre deux listes de réel et renvoie un réel correspondant à leur similarité.
Dans notre code l'une des matrices sera la transposée de la matrice tf-idf du corpus "nettoyé" et l'autre liste sera le
vecteur TF_IDF de la question.

mots_tf_idf_eleves(question): prend en patramètre une chaine de caractère correspondant à la question et renvoie le terme
dans la question ayant le tf_idf le plus élevé donc la fonction renvoie une chaine de caractère.

document_pertinent(matriceTFIDF, vecteurTFIDF, liste_nom_fichier): prend en paramètre la matriceTF_IDF (liste 2D) d'un
répertoir du type cleaned,  une liste correspondant au vecteur TFIDF de la question, une liste contenant le nom des
fichiers du répertoire étudié. La fonction renvoie une chaine de caractère correspondant au document le plus pertinent.

sous_chaine(str1,str2): orend en paramètre deux chaines de caractères et renvoie un booléen

extraire_premiere_phrase_max_tf_idf(question) : prend en paramètre uen chaine de caractère correspondant à la questionn
et renvoie une chaine de caractère correspondant à la phrase répondanr le mieux à la question

ameliorer_reponse(question): prend en paramètre une question soit une chaine carcatère et renvoie une autre chaine de
caractère correspond à un mot clé concaténé à la phrase extraite de la fonction précédente.
