class Note:
    def __init__(self, name ,valeur, coeff):
        self.name = name
        self.valeur = valeur
        self.coeff = coeff
    
    def __str__(self):
        return self.name + ': ' + str(self.valeur)

    def getNom(self):
        return self.name
        
    def getValeur(self):
        return self.valeur

    def setValeur(self, valeur):
        self.valeur = valeur

    def getCoeff(self):
        return self.coeff