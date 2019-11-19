import player as p
import regex as re
import io

class RatingList:
    def __init__(self, name: str, date: str, headline: str):
        self.name = name
        self.date = date
        self.headline = headline
        self.ratingList = []
    def addPlayer(self, player: p.Player):
        if player in self.ratingList:
            raise Exception("Error: There is already a player with that name in the list!")
            return None
        self.ratingList.append(player)
    def removePlayer(self,player: str):
        for existingPlayer in self.ratingList:
            remove = False
            if existingPlayer.getName() == player:
                self.ratingList.remove(existingPlayer)
                remove = True
        if not remove:
            print("There is no player with that name in the list")
    def getList(self):
        return self.ratingList
    def getHeadline(self):
        return self.headline
    def getName(self):
        return self.name
    def setName(self,newname: str):
        self.name = newname
    def order(self):
        l = len(self.ratingList)
        for i in range(l):
            for j in range(l):
                if p.comesBeforePlayer(self.ratingList[i], self.ratingList[j]):
                    self.ratingList[i], self.ratingList[j] = self.ratingList[j], self.ratingList[i]
    def toString(self):
        s = self.headline + " " + self.date + "\n"
        for player in self.ratingList:
            s += player.getName() + " " + str(player.getRating()) + "\n"
        return s

def words(text: str): return re.findall('[\p{\S}]+', text)

def listFromTxt(fileName: str):
    file = io.open(fileName,"r",encoding='utf-8')
    text = words(file.read())
    file.close()
    print(text)
    headline = str(text[0])
    date = str(text[1]) + " " + str(text[2])
    list = RatingList(fileName, date, headline)
    for i in range(3,len(text),3):
        name = text[i] + " " + text[i+1]
        rating = text[i + 2]
        #print(name)
        #print(rating)
        list.addPlayer(p.Player(name,int(rating)))
    return list

def writeToTxt(fileName: str,ratingList: RatingList):
    file = io.open(fileName, "w", encoding= 'utf-8')
    file.write(ratingList.toString())
    file.close()