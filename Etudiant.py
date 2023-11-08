class Etudiant:
    def __init__(self, nom, matieresListe, numeroEtudiant=None, discordID=None):
        self.nom = nom
        self.matieresListe = matieresListe
        self.numeroEtudiant = numeroEtudiant
        self.discordID = discordID

    def getNom(self):
        return self.nom
    
    def getNumeroEtudiant(self):
        return self.numeroEtudiant
    
    def getDiscordID(self):
        return self.discordID

    def getMoyenne(self):
        sum = 0
        for elem in self.matieresListe:
            sum += elem.getMoyenne() * elem.getCoeff()
        return sum
    
    def addMatiere(self, matiere):
        if matiere not in self.matieresListe:
            self.matieresListe.append(matiere)
    
    def getMatieresListe(self):
        return self.matieresListe
        
    def __str__(self):
        return self.nom + " discordID: " + str(self.discordID)
    
    def updateMatiere(self, matiere):
        for i in range(len(self.matieresListe)):
            if self.matieresListe[i].equals(matiere): # same name
                self.matieresListe[i] = matiere
                print("ok")
    
    def getAllNotes(self):
        txt = ''
        for matiere in self.getMatieresListe():
            txt += "-" + matiere.getNom() + ":\n" + str(matiere) + "\n"
        return txt
    
            