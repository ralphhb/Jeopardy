import pygame, DailyDoubleCheck, Button, Answer, EventHandler, ValidateWager, time

class Question:
    def __init__(self, screen, players):
        self.button = Button.Button(players, screen)
        self.background = "background.mid"
        self.buzzer = "TIMESUP.WAV"
        self.ddMusic = "dailyDouble.wav"
        self.ddImage = "dailyDouble2.jpg"
        self.font = pygame.font.SysFont(None, 48)
        self.screen = screen
        self.players = players
        # these needed?
        self.xCoord = int(screen.get_rect().width * .85)
        self.yCoord = int(screen.get_rect().height / 10)
        self.answer = Answer.Answer(screen, players)
        self.event = EventHandler.EventHandler()
        self.validate = ValidateWager.ValidateWager(self.players, self.screen)
        self.clock = pygame.time.Clock()
        self.message = "Which player will wager on this Daily Double?"
 
    def ddCheck(self, question, box, doubleJeopardy, ignorePlayers, gameSetupObject, dd):
        if dd == True:
            pygame.mixer.music.load(self.ddMusic)
            image = pygame.image.load(self.ddImage)
            pygame.mixer.music.play()
            width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
            x = int((width - 1075) / 2)
            y = int((height - 750) / 2)
            self.screen.fill((14,27,121))
            self.screen.blit(image, (x, y))
            pygame.display.flip()
            pygame.time.delay(4000)
            self.screen.fill((14,27,121))
            self.createDailyDoubleMessage(self.message, ignorePlayers, question, box, doubleJeopardy, gameSetupObject, dd)

        else:
            self.ask(question, box, doubleJeopardy, ignorePlayers, gameSetupObject, dd, -1)

    def ask(self, question, box, doubleJeopardy, ignorePlayers, gameSetupObject, dd, num):
        playerNum = num
        box.setBeenClicked()
        pygame.mixer.music.stop()
        pygame.mixer.music.load(self.background)
        timesUp = pygame.mixer.Sound(self.buzzer)
        pygame.mixer.music.play(-1,0.0)
        square = self.button.makeBox(box.getQuestion(doubleJeopardy))
        if dd == False:
            money = box.getPoints(doubleJeopardy)
            teamButtons = self.button.makePlayerBoxes(ignorePlayers)
            self.drawBoard(square, teamButtons)
        else:
            self.drawBoard2(square)
            self.answer.answer(playerNum, box, doubleJeopardy, gameSetupObject, ignorePlayers)
            
        start, timeLimit = self.setTimer(ignorePlayers)
        timer = True
        redraw = True
           
        #Create a box showing the time left
        pygame.time.set_timer(pygame.MOUSEMOTION, 200)
        while timer:
            drawButtons = True
            if redraw:
                teamButtons = self.button.makePlayerBoxes(ignorePlayers)
                self.drawBoard(square, teamButtons)
                redraw = False                
            coordHolder = self.event.questionEvents()
            for i in xrange(len(teamButtons)):
                if self.isClicked(coordHolder[0], coordHolder[1],teamButtons[i][1]):
                    playerNum = self.getPlayerNum(i, ignorePlayers)
                    pygame.mixer.music.stop()
                    self.answer.answer(playerNum, box, doubleJeopardy, gameSetupObject, ignorePlayers)
                    drawButtons = False
                    start, timeLimit = self.setTimer(ignorePlayers)
                    pygame.mixer.music.play(-1,0.0)                            
                    redraw = True
            if (time.time() - start) <= timeLimit and timer:
                timeLeft = (timeLimit - (time.time() - start))
                self.screen.fill((14,27,121))
                timeButton = self.button.makePlacedButton(str(int(timeLeft)), (self.xCoord, self.yCoord))
                self.screen.blit(square[0], square[1])
                if drawButtons == True:
                    for i in xrange(len(teamButtons)):
                        self.screen.blit(teamButtons[i][0], teamButtons[i][1])
                self.screen.blit(timeButton[0], timeButton[1])
            #If timer runs out
            if (time.time() - start >= timeLimit):
                timesUp.play
                pygame.mixer.music.stop()
                timer = False
            pygame.display.update()
            self.clock.tick(60)
        pygame.mixer.music.stop()
        self.answer.displayAnswer(playerNum, box, doubleJeopardy, gameSetupObject)

    """This method shows a message asking you to select a player for the daily double question.  It also renders the name boxes."""     
    def createDailyDoubleMessage(self, message, ignorePlayers, question, box, doubleJeopardy, gameSetupObject, dd):
        current_string = []
        #fontobject = pygame.font.Font(None, 32)
        pygame.draw.rect(self.screen, (0,0,0),
            ((self.screen.get_width() / 2) - 100,
            (self.screen.get_height() / 2) - 500, 200, 20), 0)

        teamButtons = self.button.makePlayerBoxes(ignorePlayers)               
        self.screen.blit(self.font.render(message, 1, (195,174,46)),
            ((self.screen.get_width() / 2) - 375, self.screen.get_height() / 2))
        for i in xrange(len(teamButtons)):
            self.screen.blit(teamButtons[i][0], teamButtons[i][1])
        
        pygame.display.flip()
        run = True
        while run: 
            temp = self.event.handleBoardEvents()
            for i in xrange(len(teamButtons)):
                if self.isClicked(temp[0], temp[1], teamButtons[i][1]):
                    playerNum = self.getPlayerNum(i, ignorePlayers)
                    self.screen.fill((14,27,121))
                    message = "Enter your wager: $"
                    run = False
                    self.createDailyDoubleText(message, current_string, playerNum, question, box, doubleJeopardy, ignorePlayers, gameSetupObject, dd)



    """This is where you enter your wager."""
    def createDailyDoubleText(self, message, current_string, playerNum, question, box, doubleJeopardy, ignorePlayers, gameSetupObject, dd):
        #fontobject = pygame.font.Font(None, 32)
        pygame.draw.rect(self.screen, (0,0,0),
            ((self.screen.get_width() / 2) - 100,
            (self.screen.get_height() / 2) - 500, 200, 20), 0)

                        
        self.screen.blit(self.font.render(message + "".join(current_string), 1, (195,174,46)),
            ((self.screen.get_width() / 2) - 175, self.screen.get_height() / 2))
        pygame.display.flip()
        runner = True
        while runner:
            temp = self.event.handleDDText()
            if temp == "erase":
                current_string = current_string[:-1]
                self.screen.fill((14,27,121))
                self.screen.blit(self.font.render(message + "".join(current_string), 1, (195,174,46)),
                    ((self.screen.get_width() / 2) - 175, self.screen.get_height() / 2))
                pygame.display.flip()
            elif temp == "end":
                self.validate.wagerValidate(current_string, playerNum, question, box, doubleJeopardy, ignorePlayers, gameSetupObject, dd)
                self.screen.fill((14,27,121))
                runner = False
            else:
                if len(current_string) <= 5:
                    current_string.append(chr(temp))
                    self.screen.blit(self.font.render(message + "".join(current_string), 1, (195,174,46)),
                    ((self.screen.get_width() / 2) - 175, self.screen.get_height() / 2))
                    pygame.display.flip()
        self.createDailyDoubleText(message, current_string, playerNum, question, box, doubleJeopardy, ignorePlayers, gameSetupObject, dd)

    """sets the current time, and timeLimit. Used in the ask loop, called before start, and after each wrong answer"""
    def setTimer(self, ignorePlayers):
        start = time.time()
        #If ignore players has members, it is not the first time the question is asked, so reduce the timer
        if ignorePlayers[0] > -1:
            timeLimit = 15
        else:
            timeLimit = 31
        return start, timeLimit
        

    
    """used when a player button is selected to answer a question. Ensures that indexes from players[] is inserted
    into ignorePlayers[]. The main if/else statement is for 3 or 2 player games"""
    def getPlayerNum(self, num, ignorePlayers):
        playerNum = -1
        #for 3 player game
        if len(ignorePlayers) == 2:
            #if 1 player ignored
            if ignorePlayers[0] > -1 and ignorePlayers[1] == -1:
                if ignorePlayers[0] == 0:
                    if num == 0:
                        playerNum = 1
                    else:
                        playerNum = 2
                elif ignorePlayers[0] == 1:
                    if num == 0:
                        playerNum = 0
                    else:
                        playerNum = 2
                else:
                    if num == 0:
                        playerNum = 0
                    else:
                        playerNum = 1
            elif ignorePlayers[0] > -1 and ignorePlayers[1] > -1:
                if ignorePlayers[0] == 2:
                    if ignorePlayers[1] == 1:
                        playerNum = 0
                    else:
                        playerNum = 1
                elif ignorePlayers[0] == 0:
                    if ignorePlayers[1] == 1:
                        playerNum = 2
                    else:
                        playerNum = 1
                elif ignorePlayers[0] == 1:
                    if ignorePlayers[1] == 2:
                        playerNum = 0
                    else:
                        playerNum = 2
            #if no players ignored
            else:
                playerNum = num
        #for 2 player game
        else:
            if ignorePlayers[0] < 0:
                playerNum = num
            else:
                playerNum = ignorePlayers[0]
        return playerNum
    
    def drawBoard2(self, square):
        self.screen.fill((14,27,121))
        self.screen.blit(square[0], square[1])
        pygame.display.update()
        
    """draws the main board. Used before start of ask loop, and after each wrong answer"""
    def drawBoard(self, square, teamButtons):
        self.screen.fill((14,27,121))
        self.screen.blit(square[0], square[1])
        for i in xrange(len(teamButtons)):
            self.screen.blit(teamButtons[i][0], teamButtons[i][1])
        pygame.display.update()

    

    """This method is similar to isMenuClicked, it serves the same purpose for all other buttons
    If the button was clicked on, returns True, else false"""
    def isClicked(self, x, y, button):
        if (x > button.left) and (x < button.right) and (y > button.top) and (y < button.bottom):
            return True
        return False


