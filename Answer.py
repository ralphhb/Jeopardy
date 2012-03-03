import pygame, Button, GameSetup, EventHandler

class Answer:
    def __init__(self, screen, players):
        self.screen = screen
        self.player = players
        self.button = Button.Button(self.player, self.screen)
        self.event = EventHandler.EventHandler()
    
    """answer runs letting selected team answer a question right or wrong.  A player's money is also adjusted here."""
    def answer(self, playerNum, box, doubleJeopardy, board, ignorePlayers):
        x = self.screen.get_rect().centerx
        x = int(x/2)
        y = self.screen.get_rect().centery
        y = int((y/2)*3)
        team = self.button.makeBox("How did " + self.player[playerNum].getName() + " answer?")
        correct = self.button.makePlacedButton("Correct", (x, y))
        wrong = self.button.makePlacedButton("Wrong", ((x*3),y))
        money = box.getPoints(board.getDoubleJeopardy())
        self.screen.fill((14,27,121))
        self.screen.blit(team[0], team[1])
        self.screen.blit(correct[0], correct[1])
        self.screen.blit(wrong[0], wrong[1])
        pygame.display.update()
        answerLoop = True
        print(playerNum)
        while answerLoop:
            coords = self.event.handleBoardEvents()
            if self.isClicked(coords[0],coords[1], correct[1]):
                if self.player[playerNum].getWager() != -1:
                    self.player[playerNum].setMoney(self.player[playerNum].getWager())
                    self.player[playerNum].setWager(-1)
                    answerLoop = False
                else:
                    self.player[playerNum].setMoney(money)
                answerLoop = False
                
            elif self.isClicked(coords[0],coords[1], wrong[1]):
                if self.player[playerNum].getWager() != -1:
                    self.player[playerNum].setMoney(-self.player[playerNum].getWager())
                    self.player[playerNum].setWager(-1)
                    self.displayAnswer(playerNum, box, doubleJeopardy, board)   
                else:            
                    self.player[playerNum].setMoney(-money)
                #for 3 players
                if len(self.player) == 3:
                    #end turn loop if 3rd guess wrong
                        if ignorePlayers[1] > -1:
                            break
                        if ignorePlayers[0] > -1:
                            ignorePlayers[1] = playerNum
                        else:
                            ignorePlayers[0] = playerNum
        
                #for 2 players
                else:
                    if ignorePlayers[0] > -1:
                        return True
                    else:
                        ignorePlayers[0] = playerNum
                return False
        self.displayAnswer(playerNum, box, doubleJeopardy, board)
        
                
        
        
        
        
    """This method shows the answer, the current scores, and gives a link back to the board."""   
    def displayAnswer(self, playerNum, box, doubleJeopardy, board):
                
        pygame.display.update()
        x = self.screen.get_rect().centerx
        y = self.screen.get_rect().centery
        y = y/2
        answer = self.button.makeBox(box.getAnswer(board.getDoubleJeopardy))
        #for when timer expires and no player tries to answer the question
        if playerNum > -1:
            points = self.button.makePlacedButton(str(self.player[playerNum].getMoney()), (x, y))
        mainScreen = self.button.makePlacedButton("Back to Questions", (x , y*3))
        playerPlates, playerButtons = self.button.getPlayerButtons()
        self.screen.fill((14,27,121))
        self.screen.blit(answer[0], answer[1])
        #for when timer expires and no player tries to answer the question
        if playerNum > -1:
            self.screen.blit(points[0], points[1])
        self.screen.blit(mainScreen[0], mainScreen[1])

        for i in xrange(len(playerPlates)):
            self.screen.blit(playerPlates[i], playerButtons[i])
        pygame.display.update()                  

        #board.setIsItOverYet(1)
        #If true, sets the game up for round2 - double jeopardy
        #if board.getIsItOverYet == 30 and board.getDoubleJeopardy == False:
            #board.setDoubleJeopardy(True)
            #for i in xrange(36):
                #self.box[i].setBeenClicked()           
            #board.resetIsItOverYet()
        show = True    
        
        while show:
            temp = self.event.handleBoardEvents()
            if self.isClicked(temp[0], temp[1], mainScreen[1]):
                show = False
        board.showBoard(board.getBox(), board)

    """This method is similar to isMenuClicked, it serves the same purpose for all other buttons
    If the button was clicked on, returns True, else false"""
    def isClicked(self, x, y, button):
        if (x > button.left) and (x < button.right) and (y > button.top) and (y < button.bottom):
            return True
        return False
