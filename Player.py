class Player:
    def __init__(self, name):

        self.money = 0
        self.name = name
        self.wager = -1
        
    def getMoney(self):
        return self.money

    def setMoney(self, amount):
        self.money += amount

    def getName(self):
        return self.name

    def getWager(self):
        return self.wager

    def setWager(self, amount):
        self.wager = amount
