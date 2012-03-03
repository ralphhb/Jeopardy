import pygame, glob, string, EventHandler

"""This class is used to run the intro screen"""    
class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.x = -10
        self.y = 300
        self.speed_init = 10
        self.speed = self.speed_init
        self.sprite = glob.glob("walk_*.png")
        self.sprite.sort()
        self.sprite_max = len(self.sprite)-1
        self.img = pygame.image.load(self.sprite[0])
        self.sprite_pos = 0
        self.event = EventHandler.EventHandler()
        
    def startMenu(self):
        jp = pygame.image.load('jeopardy.png')
        screenX,screenY = self.screen.get_width(), self.screen.get_height()
        image = pygame.Rect(250,25,200,screenY)
        Font = pygame.font.SysFont(None,50)
        stretch = pygame.transform.scale(jp,(500,350))
        buttonA = Font.render("Start",True,(195,174,46))
        buttonR = buttonA.get_rect()
        buttonR.centerx = self.screen.get_rect().centerx
        buttonR.centery = 400
        notStarted = True
        self.move(stretch, image, buttonA, buttonR)
        while notStarted:
            temp = self.event.getNames()
            x = temp[0]
            y = temp[1]
            startYet = self.button(x, y, buttonR)
            if startYet == True:
                notStarted = False

    def move(self, stretch, image, buttonA, buttonR):
        clock = pygame.time.Clock()
        pygame.mixer.music.load('background.mid')
        pygame.mixer.music.play(-1, 0.0)
        move = -10
        while move < 200:
            clock.tick(120)
            self.screen.fill((14,27,121))
            self.screen.blit(stretch, image)
            self.screen.blit(buttonA, buttonR)
            self.update(1, self.screen)
            move +=1
            pygame.display.update()
        
    """This method changes animation images """
    def update(self, pos, screen):
        
        if pos != 0:
            self.speed -= 1
            self.x += pos
            if self.speed == 0:
                if self.x == 200:
                    self.img = pygame.image.load("point.png")
                else:
                    self.img = pygame.image.load(self.sprite[self.sprite_pos])
                    self.speed = self.speed_init
            
                if self.sprite_pos == self.sprite_max:
                    self.sprite_pos = 0
                else:
                    self.sprite_pos += pos
        screen.blit(self.img,(self.x, self.y))


    """This method used for keyboard input to name the palyer objects"""
    def user_input(self, screen, question):
        cur_string = []
        self.show_box(screen, question + ": " + string.join(cur_string,""))
        pygame.display.update()
        nameNeeded = True
        while nameNeeded == True:
            
            sentinelChecker = self.event.getKeyInput(cur_string)
            if sentinelChecker != "Zippity Bop Bop Bananas":
                cur_string = sentinelChecker
                self.show_box(screen, question + ": " + string.join(cur_string,""))
                pygame.display.update()
            else:
                nameNeeded = False       
                return string.join(cur_string,"")



    """Assists user_input() by drawing the input screen"""
    def show_box(self, screen, message):
        fontobject = pygame.font.Font(None,50)
        screen.fill((14,27,121))
        if len(message) != 0:
            screen.blit(fontobject.render(message, 1, (195,174,46)),((screen.get_width() / 2)-150, (screen.get_height() / 2)))
        pygame.display.flip()

    """Assists user_input() by sensing mouse events"""
    def button(self, x, y, rect):
        if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
            return True
        else:
            return False
