from fonction_de_base import*

res= transposee(matrice_tf_idf('cleaned'))
for elem in res:
    for val in elem:
        print(val, end="\t")
    print()
