import pygame, Board

class EventHandler():
    def __init__(self):
        pass
    
    def handleBoardEvents(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    run = False
                    return x, y
                
                             
                
                

        ###From ask
    def questionEvents(self):
        timer = True
        
        while timer:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYUP and event.type == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEMOTION:
                    x = 100
                    y = 100
                    timer = False
                    return x, y
                if event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    timer = False
                    return x, y
                    
    def extraneousStuff(self):                          
            
            #end ask

            ###dailyDoubleQuestion
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYUP and event.type == K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    if self.isClicked(x,y, correct[1]):
                        pygame.mixer.music.stop()
                        if self.wagered == True:
                            self.players[playerNum].setMoney(int(self.players[playerNum].getWager()))
                            self.wagered = False
                            self.displayAnswer(playerNum)
                            
                        else:
                            self.players[playerNum].setMoney(money)
                        return True
                    if self.isClicked(x,y, wrong[1]):
                        pygame.mixer.music.stop()
                        if self.wagered == True:
                            self.players[playerNum].setMoney(int(-self.players[playerNum].getWager()))
                            self.wagered = False
                            self.displayAnswer(playerNum)
                            
                        else:
                            self.players[playerNum].setMoney(-money)
                        return False
                         
                            
                                 
            """Create and box showing the time left"""
            if (time.time() - start) <= timeLimit and timer:
                timeLeft = (timeLimit - (time.time() - start))
                timeButton = self.makePlacedButton(str(int(timeLeft)), (xCoord, yCoord))
                self.screen.fill((14,27,121))
                self.screen.blit(square[0], square[1])
                for i in xrange(len(teamButtons)):
                    self.screen.blit(teamButtons[i][0], teamButtons[i][1])
                self.screen.blit(timeButton[0], timeButton[1])
                
            """If timer runs out"""
            if (time.time() - start >= timeLimit):
                timesUp.play
                pygame.mixer.music.stop()
                timer = False
                run = False
                self.players[playerNum].setMoney(int(-self.players[playerNum].getWager()))

            pygame.display.update()
            mainClock.tick(60)
            #end dailyDoubleQuestion

    def handleDDText(self):
        show = True
        while show:
            inkey = self.getKey()
            if inkey == pygame.K_BACKSPACE:
                return "erase"
            elif inkey == pygame.K_RETURN:
                show = False
                return "end"
            elif inkey <= 127:
                        return inkey
                        
    #end dailyDoubleText
    def extraneousShit(self):
        #createDailyDoubleMessage
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYUP and key.type == K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    for i in xrange(len(teamButtons)):
                        if self.isClicked(x,y,teamButtons[i][1]):
                            playerNum = self.getPlayerNum(i)
                            self.screen.fill((14,27,121))
                            message = "Enter your wager: $"
                            self.createDailyDoubleText(message, current_string, playerNum)
                            return False
                        #end createDailyDoubleMessage

            #answer
            run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYUP and event.type == K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    if self.isClicked(x,y, correct[1]):
                        self.players[playerNum].setMoney(money)
                        return True
                    if self.isClicked(x,y, wrong[1]):
                        self.players[playerNum].setMoney(-money)
                        #for 3 players
                        if len(self.players) == 3:
                            #end turn loop if 3rd guess wrong
                            if self.ignorePlayers[1] > -1:
                                return True
                            if self.ignorePlayers[0] > -1:
                                self.ignorePlayers[1] = playerNum
                            else:
                                self.ignorePlayers[0] = playerNum
                        #for 2 players
                        else:
                            if self.ignorePlayers[0] > -1:
                                return True
                            else:
                                self.ignorePlayers[0] = playerNum
                        return False
                    #end answer

    def getNames(self):
        #from menu constructor
        a=True
        while a:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    #sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        #sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    a=False
                    return (x, y)                        
                        
    def getKeyInput(self, current_string):
        #from Menu.user_input
        #while 1:
        inkey = self.getKey()
        if inkey == pygame.K_BACKSPACE:
            current_string = current_string[0:-1]
            return current_string
        elif inkey == pygame.K_RETURN:
            return "Zippity Bop Bop Bananas"
        elif inkey <= 127:
            current_string.append(chr(inkey))
            return current_string
        #show_box(screen, question + ": " + string.join(current_string,""))
        pygame.display.update()
        #end Menu.user_input


    """Assists user_input() to get keyboard input"""
    def getKey(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return event.key
                

                
