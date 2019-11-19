from datetime import time
from tkinter.filedialog import Open
import regex as re
import sys
import menus as m
import player as p
import ratinglist as l

__author__ = "Daniel Jogstad"


def test():
    daniel = p.Player("Daniel Jogstad", 1600)
    martin = p.Player("Martin Jogstad", 1599)
    carlsen = p.Player("Magnus Carlsen", 2874)
    mragel = p.Player("Mragel Vrillestad", 800)
    nemesis = p.Player("A. Player", 1600)
    ratingList = l.RatingList("test.txt","23/9 2019", "Eslövstoppen")
    ratingList.addPlayer(daniel)
    ratingList.addPlayer(martin)
    ratingList.addPlayer(carlsen)
    ratingList.addPlayer(nemesis)
    ratingList.addPlayer(mragel)
    ratingList.order()
    ratingList.removePlayer("Mragel Vrillestad")
    l.writeToTxt("test.txt", ratingList)
    print(ratingList.toString())
    ratingList2 = l.listFromTxt("test.txt")
    print(ratingList2.toString())

def run():
    #test()
    m.welcome()
def main():
    run()
if __name__ == "__main__":
    main()
