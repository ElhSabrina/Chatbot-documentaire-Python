dico={'s':1,'l':1,'p':2}
max= 1
for cle, valeur in dico.items():
    if dico[cle] == max:
        print(cle)