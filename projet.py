# 13/12/2025,  Master 01 microbiologie et contrôle de qualité,  chef de projet: benachenhou douaa 
#herir nesrine
#Hocine Hadil
#Ayed Zeddam Abir
#Derni Salima

import pandas as pd

# Donner : Séquence,Longueur,Pourcentage GC
data = {
    "Séquence":  ["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"],
    "Longueur": [12, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
}
# herir nesrine 
# 1) Création et affichage d'une DataFrame (tableau pandans)
nh = pd.DataFrame(data)
print("********** Création et affichage *********","\n""\n")

# Affinage du tableau
print("Tableau des séquences ADN :", "\n")
print(nh, "\n""\n")







# benachenhou douaa 
# 4) Calculer la moyenne du pourcentage de GC
print("*********** Calcul de la moyenne ***********", "\n")
average_gc = nh["Pourcentage GC"].mean()
print(f"pourcentage moyen de GC : {average_gc:.3f}%", "\n")

#ayad Zeddam abir
#5) Ajouter d'un colonne "Catégorie GC"
print("*********** Ajoute d'une colonne Catégorie GC ***********", "\n")
def Catégorie_GC (GC_precent):
 if GC_precent>55:
    return "Riche"
 elif 45<= GC_precent<=55:
    return "moyen"
 else :
    return "faible"
     
#Derni Salima
nh["Catégorie GC"] = nh["Pourcentage GC"].apply(Catégorie_GC)
print("********** 5)Tableau avec Catégorie GC *******")
print(nh, "\n")





#ayad Zeddam abir
#6) Ajouter une colonne donnant le nombre de G
nh["nombre de G"] = nh["Séquence"].str.count("G")
print("********** 6) Nombre de G ajoutés **********")
print(nh, "\n")
