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

# Hocine Hadil

# 2 sélection et afficher uniquement de colone "longueur"
longueur = nh["Longueur"]
print("********* 2)  Affichage de colonne [Longueur] ********* ")
print(nh["Longueur"], "\n")

# Derni Salima
# 3 filtrer les séquences avec une longueur supérieur à 10
print("********* Filtrer avec Longueur *********")
filtered_nh = nh[nh["Longueur"] >10]
print(filtered_nh, "\n")

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
     
# Derni Salima
nh["Catégorie GC"] = nh["Pourcentage GC"].apply(Catégorie_GC)
print("********** 5)Tableau avec Catégorie GC *******")
print(nh, "\n")

#ayad Zeddam abir
#6) Ajouter une colonne donnant le nombre de G
nh["nombre de G"] = nh["Séquence"].str.count("G")
print("********** 6) Nombre de G ajoutés **********")
print(nh, "\n")
# Hocine Hadil
#7) calculer de l'écart-type du pourcentage GC
print("********** Calcule de l'écart-type du Pourcentage GC********")
écart-type_gc = nh["Pourcentage GC"].mean()
print(f"Écart-type du Pourcentage GC : {écart-type_gc:.3f}%", "\n")
