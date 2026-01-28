# My Chat Bot (Python)

Projet en Python visant à analyser un corpus de fichiers texte (répertoire `cleaned`) et à répondre à des questions utilisateur à partir des documents, en combinant recherche automatique et scoring **TF IDF**.

## Groupe
Sabrina El Hassani  
Lucy Gros

## Objectif
- Analyser des fichiers texte d’un répertoire
- Construire une représentation TF IDF du corpus
- Identifier le document le plus pertinent pour une question
- Extraire une réponse à partir du contenu et améliorer la formulation

## Fonctionnement général
1. Nettoyage des documents (minuscules, suppression caractères spéciaux) pour obtenir un répertoire `cleaned`
2. Calcul des scores TF, IDF et de la matrice TF IDF du corpus
3. Tokenisation de la question et calcul de son vecteur TF IDF
4. Mesure de similarité (cosine) entre question et documents
5. Sélection du document le plus pertinent et extraction d’une phrase réponse

## Contenu du dépôt
- `main.py` : programme principal avec menu d’exécution
- `FonctionsColonnes.h/c` et `FonctionsCdataFrame.h/c` ne concernent pas ce projet (à supprimer si présents)
- `cleaned/` : corpus nettoyé utilisé par le programme
- `report/Chat_Bot_Python.pdf` : rapport du projet

## Fonctions principales
### Prétraitement et analyse du corpus
- `list_of_files(repertoire, extension)` : liste les fichiers du répertoire
- `conversion_car(texte)` : normalise un texte (minuscules, suppression caractères spéciaux)
- `occur(chaine)` : retourne les occurrences des mots
- `tf(fichier)` et `tf_texte(texte)` : calcule le TF
- `idf(repertoire)` : calcule l’IDF du corpus
- `matrice_tf_idf(repertoire)` : construit la matrice TF IDF

### Recherche et similarité
- `tokenisation(question)` : découpe une question en mots
- `recherche_mot_question(liste, repertoire)` : mots communs entre question et corpus
- `calcul_vecteur_tf_idf(question, matrice)` : vecteur TF IDF de la question
- `produit_scalaire(A, B)` et `norme_vecteur(A)` : utilitaires mathématiques
- `similarite(A, B)` : similarité cosinus
- `document_pertinent(matriceTFIDF, vecteurTFIDF, liste_nom_fichier)` : sélection du document le plus pertinent

### Génération de réponse
- `mots_tf_idf_eleves(question)` : mot clé le plus important de la question
- `extraire_premiere_phrase_max_tf_idf(question)` : extrait une phrase pertinente du document
- `ameliorer_reponse(question)` : améliore la réponse finale (mot clé + phrase)

## Exécution
1. Placer les fichiers texte dans un dossier `cleaned`
2. Lancer le programme principal
```bash
python main.py

