class TradingCardManager:
    cardList = []

    @staticmethod
    def addCard(card):
        TradingCardManager.cardList.append(card)

    @staticmethod
    def getCardList():
        return TradingCardManager.cardList

    @staticmethod
    def displayAllCards():
        printBuffer = ""

        for card in TradingCardManager.cardList:
            printBuffer += (str(card) + '\n')

        print(printBuffer)

    @staticmethod #Error handling
    def findByName():
        print("Enter name of card: ")
        userIn = input("Name: ")

        for card in TradingCardManager.cardList:
            if card.getName() == userIn:
                print(card)
                return card

        print("card not found")
        return None

    @staticmethod
    def inputSan(value):
         val = None
         val = value.strip()
         return val

    @staticmethod
    def findAllNames():
        localList = []

        userIn = input("Name: ")
        userIn = userIn.strip()

        for card in TradingCardManager.cardList:
            if card.getName() == userIn:
                localList.append(card)

        if not localList:
            print("cards not found")
            return None

        return localList

    @staticmethod
    def amendCards():
        # Find card by name
        print("Enter card: ")
        userIn = input("Name: ")
        userIn = userIn.strip()

        localCard = None

        for myCard in TradingCardManager.cardList:
            if myCard.getName() == userIn:
                localCard = myCard
                break

        # Change details
        print("Enter New Details")
        newName = input("Name: ")

        newHP = None

        while newHP is None:
            try:
                newHP = int(input("New HP: "))
            except ValueError:
                print("Not an int")
                newHP = None

        localCard.setName(newName)
        localCard.setHP(newHP)

        print(localCard)

        return True

'''
#TradingCardManager.add_card(Card("Thor", 9, 9, 8))
'''

