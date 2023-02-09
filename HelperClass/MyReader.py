import csv
from MyObjects.Trading_Card_Manager import *
from MyObjects.Card import *
class MyReader:

    @staticmethod
    def readInFiles(readPath):

        with open(readPath, newline= '') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for row in reader:
                TradingCardManager.addCard(Cards(*row))

    @staticmethod
    def writeContentToFile(writePath):
        localCardList = TradingCardManager.getCardList()

        writeBuffer = ""
        for card in localCardList:
            writeBuffer += (str(card) + '\n')

            with open(writePath, 'w', encoding='UTF8') as csvfile:
                csvfile.write(writeBuffer)