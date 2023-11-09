import pickle, discord
from Note import *
from Matiere import *
from Etudiant import *

def storeEtudiantsListe(etudiantsListe):
    output = open("dataEtudiants.pickle","wb")
    pickle.dump(etudiantsListe, output)
    output.close()

def loadEtudiantsListe():
    input = open("dataEtudiants.pickle","rb")
    etudiantsListe = pickle.load(input)
    input.close()
    return etudiantsListe   

def getEtudiant(ctx, etudiantsList):
    for etudiant in etudiantsList:
        if etudiant.getDiscordID() == ctx.message.author.id:
            return etudiant
    return None

def generateEtudiant(name, discordID):
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

    etudiant = Etudiant(name, matieresList, discordID=discordID)
    return etudiant

def generateProfile(etudiant):
    embed = discord.Embed(title=etudiant.getNom(), description="Voilà un résumé de tes notes !")
    for matiere in etudiant.getMatieresListe():
        embed.add_field(name=matiere.getNom(), value=str(matiere))
    return embed

def generateBlueText(txt):
    return "```CSS\n- " + str(txt) + " -\n```"

def generateRedText(txt):
    return "```diff\n- " + str(txt) + " -\n```"

def generateMoyennes(etudiant):
    embed = discord.Embed(title=etudiant.getNom(), description="Voilà tes moyennes !", color = discord.Color.red())
    for matiere in etudiant.getMatieresListe():
        moyenne = matiere.getMoyenne()
        if moyenne >= 10:
            embed.add_field(name=matiere.getNom(), value=generateBlueText(moyenne))
        else:
            embed.add_field(name=matiere.getNom(), value=generateRedText(moyenne))
        
    return embed


def updateEtudiantList(etudiantList, etudiant):
    for i in range(len(etudiantList)):
        if etudiantList[i].getDiscordID() == etudiant.getDiscordID():
            etudiantList[i] = etudiant
            print("OUIIIII")
            return etudiantList
    return etudiantList
