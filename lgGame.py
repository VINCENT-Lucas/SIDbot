class lgGame:
    def __init__(self, ownerID):
        self.playersList = [ownerID]
        self.ownerID = ownerID

    def addNewPlayer(self, playerID):
        if playerID not in self.playersList:
            self.playersList.add(playerID)
        else:
            return "Ce joueur est déjà inscrit !"
    
    def removePlayer(self, playerID):
        if playerID not in self.playersList:
            self.playersList.remove(playerID)
        else:
            return "Ce joueur n'était pas déjà inscrit !"
        
    def getPlayersAmount(self):
        return len(self.playersList)
    