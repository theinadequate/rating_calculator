class Player():
    def __init__(self, insertName, insertRating):
        self.name = insertName
        self.rating = insertRating
    def getName(self):
        return self.name
    def getRating(self):
        return self.rating
    def setName(self, newName):
        self.name = newName
    def setRating(self, newRating):
        self.rating = newRating
def comesBeforePlayer(player1: Player, player2: Player):
    if player1.getRating() > player2.getRating(): return True
    if player1.getRating() == player2.getRating() and player1.getName() < player2.getName(): return True
    return False
def getNewRating(player1: Player, player2: Player, result: str):
    if result == "w":
        player1.setRating(player1.getRating() + 16)
        player2.setRating(player1.getRating() - 16)
    else:
        if result == "b":
            player2.setRating(player2.getRating() + 16)
            player1.setRating(player1.getRating() - 16)
        else:
            player1.setRating(player1.getRating() + 0)
            player2.setRating(player1.getRating() + 0)