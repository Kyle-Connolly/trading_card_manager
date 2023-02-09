from HelperClass.MyReader import *
class MyInterface:

    @staticmethod
    def run():

        # read in cards
        MyReader.readInFiles('InputFiles/input.csv')

        # display interface
        MyInterface.displayMenu()

    @staticmethod
    def displayMenu():
        print("Main Menu")
        print("1. Display")
        print("2. Search")
        print("3. Amend")
        print("\n\n")

        userIn = int(input("Enter choice: "))

        if userIn == 1:
            MyInterface.displayCards()
            MyInterface.displayMenu()
        if userIn == 2:
            MyInterface.findByName()
            MyInterface.displayMenu()
        if userIn == 3:
            MyInterface.amendCard()
            MyInterface.displayMenu()

    @staticmethod
    def displayCards():
        TradingCardManager.displayAllCards()

    @staticmethod
    def findByName():
        TradingCardManager.findByName()

    @staticmethod
    def amendCard():
        TradingCardManager.amendCards()
        MyReader.writeContentToFile('InputFiles/input.csv')