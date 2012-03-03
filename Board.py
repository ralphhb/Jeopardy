import pygame, DailyDoubleSetter, EventHandler, Question, Button

class Board:
    def __init__(self, players, screen):
        self.screen = screen
        self.box = []
        self.players = players
        self.done_image = "done.png"
        #self.background = 'background.mid'
        #self.buzzer = 'TIMESUP.WAV'
        self.boardFill = 'boardFill2.wav'
        #do we need font here?
        self.font = pygame.font.SysFont(None, 48)
        self.ignorePlayers = []
        self.doubleJeopardy = False
        self.beginRound = True
        self.isItOverYet = 0
        self.wagered = False
        self.dd1 = 0
        self.dd2 = 0
        self.dd3 = 0
        #these coords may not be needed anymore
        self.xCoord = int(self.screen.get_rect().width * .85)
        self.yCoord = int(self.screen.get_rect().height / 10)
        self.event = EventHandler.EventHandler()
        self.question = Question.Question(screen, players)
        self.button = Button.Button(players, screen)
        self.dd = False
        
    """showBoard controls the main game loop - it draws the board, and calls ask when a button is clicked on.  It checks the beginRound boolean to see whether it
should form randomly."""
    def showBoard(self, box, gSetup):
        for i in xrange(36):
            self.box.append(box[i])
        if self.dd1 == 0:
            dds = DailyDoubleSetter.DailyDoubleSetter(self.box)
            self.dd1 = dds.setDailyDoubles()
            print(self.box[self.dd1].getQuestion(self.doubleJeopardy))
            self.dd2 = dds.setDailyDoubles()
            print(self.box[self.dd2].getQuestion(self.doubleJeopardy))
            self.dd3 = dds.setDailyDoubles()
            print(self.box[self.dd3].getQuestion(self.doubleJeopardy))

        if self.isItOverYet == 30:
            self.doubleJeopardy = True
            self.beginRound = True
            self.isItOverYet = 0
            for i in xrange(36):
                self.box[i].setBeenClicked()
        self.screen.fill((14,27,121))
        pygame.display.update()
        #if self.doubleJeopardy == True and  self.is_it_over_yet == 30:
            #self.final_jeopardy()
        if self.beginRound == True:
            pygame.mixer.music.load(self.boardFill)
            pygame.mixer.music.play()
            pygame.time.delay(225)
            if len(self.players) == 3:
                self.ignorePlayers = [-1, -1]
            else:
                self.ignorePlayers = [-1]
            for i in xrange(36):
                coords = self.box[i].getCoords()
                image = pygame.image.load(self.box[i].getImage(self.doubleJeopardy))               
                frame = pygame.Rect(coords, (125, 95))
                self.box[i].setFrame(frame)
                self.screen.blit(image, frame)
                pygame.time.delay(60)
                pygame.display.flip()

            self.beginRound = False
        else:
            if len(self.players) == 3:
                self.ignorePlayers = [-1, -1]
            else:
                self.ignorePlayers = [-1]
            for i in xrange(36):
                coords = self.box[i].getCoords()
                if self.box[i].getBeenClicked() == True:
                    image = pygame.image.load(self.box[i].getImage(self.doubleJeopardy))
                else:                              
                    image = pygame.image.load(self.box[i].getImage(self.doubleJeopardy))               
                frame = pygame.Rect(coords, (125, 95))
                self.box[i].setFrame(frame)
                self.screen.blit(image, frame)

            pygame.display.flip()
                
        #mainClock = pygame.time.Clock()
        gameLoop = True
        self.dd = False
        while gameLoop:
            temp = self.event.handleBoardEvents()
            boxNum = self.isMenuClicked(temp[0], temp[1])
            if boxNum >= 0 and self.box[boxNum].getBeenClicked() == False and self.box[boxNum].getQuestion(boxNum) != "placeholder":
                    if boxNum == self.dd2 and self.doubleJeopardy or boxNum == self.dd3 and self.doubleJeopardy:
                        self.dd = True
                        gameLoop = False
                        self.isItOverYet += 1
                        self.question.ddCheck(self.question, self.box[boxNum], self.doubleJeopardy, self.ignorePlayers, gSetup, self.dd)
                    elif boxNum == self.dd1:
                        self.dd = True
                        gameLoop = False
                        self.isItOverYet += 1
                        self.question.ddCheck(self.question, self.box[boxNum], self.doubleJeopardy, self.ignorePlayers, gSetup, self.dd)
                        
                    else:
                        gameLoop = False
                        self.isItOverYet += 1
                        self.question.ddCheck(self.question, self.box[boxNum], self.doubleJeopardy, self.ignorePlayers, gSetup, self.dd)
                        
            
    
    """This method checks if a question box was clicked by iterating through the box array. Items is a
    list containing the 4 edges of the button in the order, left, right, top, bottom. If a box was clicked
    on, returns the index number of theteamButtons = self.makePlayerBoxes() box. Else returns -1"""
    def isMenuClicked(self, x, y):
        for i in self.box:
            frame = i.getFrame()
            if (x > frame.left) and (x < frame.right) and (y > frame.top) and (y < frame.bottom):
                return self.box.index(i)       
        return -1

    def setIsItOverYet(self, num):
        self.isItOverYet += 1

    def getIsItOverYet(self):
        return self.isItOverYet

    def resetIsItOverYet(self):
        self.isItOverYet = 0

    def getDoubleJeopardy(self):
        return self.doubleJeopardy

    def setDoubleJeopardy(self, state):
        self.doubleJeopardy = state

    def getBox(self):
        return self.box
    





