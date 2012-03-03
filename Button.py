import pygame

class Button:
    def __init__(self, players, screen):
        self.players = players
        self.screen = screen
        self.font = pygame.font.SysFont(None, 48)

    """similar to makeButtons but accepts a tuple containing x,y coords"""
    def makePlacedButton(self, phrase, coords):
        facePlate, button = self.makeBox(phrase)
        button.centerx = coords[0]
        button.centery = coords[1]
        return (facePlate, button)
                                                 
    """this method used to make a full screen box to display a question"""
    def makeBox(self, question):
        item = self.font.render(question, True, (195,174,46))
        item_Box = item.get_rect()
        item_Box.centerx = self.screen.get_rect().centerx
        item_Box.centery = self.screen.get_rect().centery
        return (item, item_Box)

    
    """This overloaded method makes a single button - not used for team buttons which come in threes"""
    def makeButtons(self, phrase):
        button = self.font.render(phrase, True, (195,174,46))
        button_Box = button.get_rect()
        x = self.screen.get_rect().centerx
        x = int((x/4)*3)
        y = self.screen.get_rect().centery
        y = int((y/4)*3)
        button_Box.centerx = x
        return (button, button_Box)

    """This overloaded method is used to make team buttons, it accepts a int - yModifer to identify which team number it is"""
    def makeButtons(self, phrase, xModifer):
        button = self.font.render(phrase, True, (195,174,46))
        button_Box = button.get_rect()
        x = self.screen.get_rect().centerx
        #This sets the three team buttons x coordinate at 1/4 , middle, and 3/4 across the screen
        if(xModifer == 1):
            xcoord = int(.5 * x)
        elif(xModifer == 2):
            xcoord = x
        else:
            xcoord = int(x + .5*x)
        y = self.screen.get_rect().centery
        ycoord = int((y/2)*3)
        button_Box.centerx = xcoord
        button_Box.centery = ycoord
        return (button, button_Box)

    """This creates player buttons used to display team names and how much money they have"""
    def getPlayerButtons(self):
        facePlates = []
        buttons = []
        x = self.screen.get_rect().centerx
        y = self.screen.get_rect().centery
        yCoord = int(y/3)
        xCoord = int(x/2)
        for i in xrange(len(self.players)):
            item = self.font.render(self.players[i].getName()+":"+str(self.players[i].getMoney()), True, (195,174,46))
            item_Box = item.get_rect()
            item_Box.centerx = xCoord
            item_Box.centery = yCoord
            xCoord += int(x/2)
            facePlates.append(item)
            buttons.append(item_Box)
        return facePlates, buttons


    """Makes the player boxes to be used in the ask method"""
    def makePlayerBoxes(self, ignorePlayers):
        teamButtons = []
        for i in xrange(len(self.players)):
            if ignorePlayers[0] > -1:
                if i == ignorePlayers[0]:
                    continue
                if i == ignorePlayers[1]:
                    continue
            teamButtons.append(self.makeButtons("["+self.players[i].getName() + "]", (i+1)))
        return teamButtons
