class ValidateWager:
    def __init__(self, players, screen):
        self.players = players
        self.screen = screen
        
    """Here we determine whether a placed wager is valid or not"""
    def wagerValidate(self, current_string, playerNum, question, box, doubleJeopardy, ignorePlayers, gameSetupObject, dd):
        money = self.players[playerNum].getMoney()
        myString = "".join(current_string)
        if myString.isdigit() == False:
            message = "Please try again: $"
            current_string = []
            self.screen.fill((14,27,121))
            question.createDailyDoubleText(message, current_string, playerNum, question, box, doubleJeopardy, ignorePlayers, gameSetupObject, dd)
        elif money <= 1000 and int(myString) > 1000:
            message = "Please try again: $"
            current_string = []
            self.screen.fill((14,27,121))
            question.createDailyDoubleText(message, current_string, playerNum, question, box, doubleJeopardy, ignorePlayers, gameSetupObject, dd)
        elif money <= 1000 and int(myString) <= 1000:
            self.wagered = True
            self.players[playerNum].setWager(int(myString))
            question.ask(question, box, doubleJeopardy, ignorePlayers, gameSetupObject, dd, playerNum)
        elif int(myString) > money:
            message = "Please try again: $"
            current_string = []
            self.screen.fill((14,27,121))
            question.createDailyDoubleText(message, current_string, playerNum, question, box, doubleJeopardy, ignorePlayers, gameSetupObject, dd)
        else:
            self.wagered = True
            self.players[playerNum].setWager(int(myString))
            question.ask(question, box, doubleJeopardy, ignorePlayers, gameSetupObject, dd, playerNum)
