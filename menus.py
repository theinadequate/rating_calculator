import player as p
import ratinglist as l
import sys
import regex as re

def words(text: str): return re.findall('[\p{\S}]+', text)
def exitCode():
    sys.exit()
def newListMenu():
    while True:
        print("Type in the filename of the new list as \"name.txt\", the headline (in one word) as well as the date of the list as \"??/?? ????\"")
        try:
            i = words(input())
            fileName = i[0]
            if fileName == "q":
                sys.exit()
            if fileName == "m":
                welcome()
            headline = i[1]
            date = str(i[2]) + " " + str(i[3])
            ratingList = l.RatingList(fileName,headline,date)
            useListMenu(ratingList)
        except:
            print("an error with the input occurred, please try again")
            break
def newListMenu():
    while True:
        print("Type in the filename of the new list as \"name.txt\", the headline (in one word) as well as the date of the list as \"??/?? ????\"")
        try:
            i = words(input())
            fileName = i[0]
            if fileName == "q":
                sys.exit()
            if fileName == "m":
                welcome()
            headline = i[1]
            date = str(i[2]) + " " + str(i[3])
            ratingList = l.RatingList(fileName,date,headline)
            useListMenu(ratingList)
        except:
            invalidInput()
            break
def useListMenu(ratingList: l.RatingList):
    def useListError():
        invalidInput()
        print("NOOO")
        useListMenu()
    def saveList(ratingList: l.RatingList):
        print("Input what you want to save the list as:")
        try:
            i = input()
            l.writeToTxt(i,ratingList)
            ratingList.setName(i)
        except:
            invalidInput()
            print("the data might not have been saved, try again.")
            useListMenu()
        print("List was saved!")
        useListMenu(ratingList)
    try:
        print("What would you like to do with \"" + ratingList.getName() + "\"?")
        print("Save the list: type s")
        print("Print the list: type p")
        print("Add a player to the list: type a")
        print("Delete a player in the list: press d")
        print("Edit a player in the list: press e")
        print("Add a result between two players: press r")
        print("Check added results: press c")
        print("Update the list according to the added results")
        i = input()
    except:
        invalidInput()
        print("no2")
    switcher = {
        "q": exitCode,
        "s": saveList(ratingList),
        "l": loadListMenu,
    }
    switcher.get(i, useListError)()

def welcome():
    def welcomeInvalid():
        invalidInput()
        welcome()
    print("Welcome to the rating calculator for Eslövs schackklubb!\n")
    print("Choose how to proceed:\n.")
    print("To create a list, type \"c\".")
    print("To load an existing list, type \"l\".")
    print("To get back to this menu, type \"m\"")
    print("To quit, type \"q\".")
    try:
        i = input()
    except:
        invalidInput()
        return welcome()
    switcher = {
        "q": exitCode,
        "c": newListMenu,
        "l": loadListMenu,
    }
    switcher.get(i, welcomeInvalid)()
def loadListMenu():
    print("load List")
def invalidInput():
    print("Invalid input, try again.")