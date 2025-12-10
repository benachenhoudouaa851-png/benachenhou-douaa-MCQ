# 13/12/2025,  Master 01 microbiologie et contrôle de qualité,  chef de projet: benachenhou douaa 
#herir nesrine
#Hocine Hadil
#Ayed Zeddam Abir
#Derni Salima

import pandas as pd

# Donner : Séquence,Longueur,Pourcentage GC
Data = {
    "Séquence":  ["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"]
    "Longueur": [12, 12, 12, 10, 11, 10, 10]
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
}
# herir nesrine 
# 1) Création et affichage d'une DataFrame (tableau pandans)
nh = pd.DataFrame(data)
print("***************** Création et affichage *****************","\n")
