class Matiere:
    def __init__(self, nom, listeNotes=[], coeff=1):
        self.nom = nom
        self.listeNotes = listeNotes
        self.coeff = coeff
    
    def __str__(self):
        txt = ''
        for elem in self.listeNotes:
            txt += "- " + str(elem) + "\n"
        return txt
        
    def getListeNotes(self):
        return self.listeNotes
    
    def getCoeff(self):
        return self.coeff
    
    def getNoteValue(self, noteNom):
        for elem in self.listeNotes:
            if elem.getNom().upper() == noteNom.upper():
                return elem.getValeur()
        return None

    def getNote(self, noteNom):
        for elem in self.listeNotes:
            if elem.getNom().upper() == noteNom.upper():
                return elem
        return None
    
    def equals(self, other):
        return self.nom == other.nom
    
    def setNote(self, noteNom, noteValeur):
        for elem in self.listeNotes:
            if elem.getNom().upper() == noteNom.upper():
                elem.setValeur(noteValeur)
    
    def getMoyenne(self):
        sum = 0
        for elem in self.listeNotes:
            if elem.getValeur():
                sum += elem.getCoeff() * elem.getValeur()
        return sum
    
    def getNom(self):
        return self.nom
