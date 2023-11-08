from Matiere import *
from Note import *
from Etudiant import * 

### Création des notes via Moodle

matieresList = []

# Algèbre linéaire
ccAlgebre = Note("CC", None, 0.3)
ctAlgebre = Note("CT", None, 0.7)
matieresList.append(Matiere("Algèbre linéaire", [ccAlgebre, ctAlgebre]))
# Modélisation, Conception, Développement Collaboratif
ccMCDC = Note("CC", None, 0.3)
ctMCDC = Note("CT", None, 0.7)
matieresList.append(Matiere("Modélisation, Conception, Développement Collaboratif", [ccMCDC, ctMCDC]))
# Algorithmique avancée
ccAlgo = Note("CC", None, 0.2)
cpAlgo = Note("CP", None, 0.3)
ctAlgo = Note("CT", None, 0.5)
matieresList.append(Matiere("Algorithmique avancée", [ccAlgo, cpAlgo, ctAlgo]))
# Optimisation mathématique
ccOpti = Note("CC", None, None)
ctOpti = Note("CT", None, None)
matieresList.append(Matiere("Optimisation mathématique", [ccOpti, ctOpti]))
# Transformations de modèles
ccTransfo = Note("CC", None, None)
ctTransfo = Note("CT", None, None)
matieresList.append(Matiere("Transformations de modèles", [ccTransfo, ctTransfo]))
# Data Warehouse et OLAP
ccDataWH = Note("CCTP", None, None)
ctDataWH = Note("CT", None, None)
matieresList.append(Matiere("Data Warehouse et OLAP", [ccDataWH, ctDataWH]))
# Statistique Exploratoire et apprentissage non-supervisé
ccStats = Note("CC", None, 0.3)
ctStats = Note("CT", None, 0.7)
matieresList.append(Matiere("Statistique Exploratoire et apprentissage non-supervisé", [ccStats, ctStats]))

# Création de l'étudiant

etudiant = Etudiant("VINCENT Lucas", matieresList, 22002171)
print(etudiant.getMoyenne())

'''
note1 = Note("CC1", 16, 0.3)
algoAvancee = Matiere("Algorithmique Avancée", [note1])
algoAvancee.setNote("CC1", 10)
print(algoAvancee.getNote("CC1"))
print(algoAvancee.getMoyenne())
'''

