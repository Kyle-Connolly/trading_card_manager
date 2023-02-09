# class to act as template for all Cards
class Cards:
    # constructor for Card, uses name mangling for attribute encapsulation/keeps attributes private
    # (removed attack and defense fields)
    def __init__(self, id, health):
        self.__name = id
        self.__hp = health
        # self.__attack = atk
        # self.__defense = defnse

    # ACCESSOR METHODS
    # get Card's name
    def getName(self):
        return self.__name

    def getHP(self):
        return self.__hp

    def getAttack(self):
        return self.__attack

    def getDefense(self):
        return self.__defense

    # MUTATOR METHODS
    # set Card's name to the user's input (taken through the parameter)
    def setName(self, id):
        self.__name = id

    def setHP(self, health):
        self.__hp = health

    def setAttack(self, atk):
        self.__attack = atk

    def setDefense(self, defnse):
        self.__defense = defnse

    def __str__(self):
        return str(Cards.getName(self) + "," + str(Cards.getHP(self)))