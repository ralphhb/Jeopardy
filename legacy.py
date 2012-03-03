"""Jeopardy written by Adam Hess, Ralph Busby, Michael Moseng, and Ben Stumpf
    1/25/2012
    Any misuse of this program is punishable by Alex Trebek"""
 
import pygame, random, time, sys, glob, string
from pygame.locals import *

"""The Player object is very simple, containing just three attributes and associated getters and setters"""


"""The box object holds most of the data for the program.  Each box holds its coordinates, questions, answers and images for both regular and
double jeopardy, a "done" image for when it has been clicked.  Questions, answers, and images are tuples containing the question and image for
both rounds.  There is also a boolean that tells whether a box has been clicked before, along with associated getters and setters."""



"""The board object is where almost all the logic for the game is kept.  Notable attributes include width and height, which size the screen,
the screen itself for things to be placed on, an ignorePlayers list that keeps track of the number of players, and booleans that track whether
it is double jeopardy, how long until the round is over, whether it is the beginning of a round, and whether a player has made a wager(for daily doubles
and final jeopardy"""



    """This method starts the method cascade to ask a question. It draws the question screen and the player buttons. ignorePlayers is a list
    which can contain player numbers which have already gotten the question wrong. It's values are -1, -1 by default and never exceeds size  of 2"""
   

    """This method does excactly what you might think it does,.  If the selected box is a daily double, it starts logic for that"""
    

    
    """This method listens for key input  for the wager entry method directly above."""
    
                
   

   
                
    
                
    



"""This class is used to run the intro screen"""    
class Menu:
    def __init__(self,screen):
        clock =pygame.time.Clock()
        pygame.init()
        pygame.mixer.music.load('background.mid')
        pygame.mixer.music.play(-1, 0.0)
        self.x = -10
        self.y = 300
        self.speed_init = 10
        self.speed = self.speed_init
        self.sprite = glob.glob("walk_*.png")
        self.sprite.sort()
        self.sprite_max = len(self.sprite)-1
        self.img= pygame.image.load(self.sprite[0])
        self.sprite_pos = 0
        jp = pygame.image.load('jeopardy.png')
        screenX,screenY =screen.get_width() ,screen.get_height()
        image = pygame.Rect(250,25,200,screenY)
        Font = pygame.font.SysFont(None,50)
        Stretch = pygame.transform.scale(jp,(500,350))
        buttonA = Font.render("[start]",True,(195,174,46))
        buttonR = buttonA.get_rect()
        buttonR.centerx = screen.get_rect().centerx
        buttonR.centery = 400
        pos = 1
        move = -10
        while move < 200:
            clock.tick(120)
            screen.fill((14,27,121))
            screen.blit(Stretch,image)
            screen.blit(buttonA,buttonR)
            self.update(pos,screen)
            move +=1
            pygame.display.update()

        a=True
        while a:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    if button(x,y,buttonR) == True:
                        a=False
    """This method changes animation images """
    def update(self,pos,screen):
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
def user_input(screen, question):
    pygame.font.init()
    current_string = []
    show_box(screen, question + ": " + string.join(current_string,""))
    while 1:
        inkey = getkey()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == K_RETURN:
            break
        elif inkey <= 127:
            current_string.append(chr(inkey))
        show_box(screen, question + ": " + string.join(current_string,""))
        pygame.display.update()
    return string.join(current_string,"")

"""Assists user_input() to get keyboard input"""
def getkey():
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                return event.key

"""Assists user_input() by drawing the input screen"""
def show_box(screen, message):
    fontobject = pygame.font.Font(None,50)
    screen.fill((14,27,121))
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (195,174,46)),((screen.get_width() / 2)-150, (screen.get_height() / 2)))
    pygame.display.flip()

"""Assists user_input() by sensing mouse events"""
def button(x, y, rect):
    if (x > rect.left) and (x < rect.right) and (y > rect.top) and (y < rect.bottom):
        return True
    else:
        return False


def main():
    pygame.init()
    player = []
    """This boolean tracks whether or not the boxes on the screen should appear randomly, which should only happen at the beginning of a round"""
    #below is the logic for reading in the questions and answers, and assigning them to category objects as they are made
    #open the neccessary files
    round1Qs = open('questionsA.txt','r')
    round2Qs = open('questionsB.txt','r')
    round1As = open('answersA.txt', 'r')
    round2As = open('answersB.txt', 'r')
    round1Cats = open('catA.txt','r')
    round2Cats = open('catB.txt','r')
    """Create images of each category label to pass to appropriate boxes"""
    item = round1Cats.readline()
    item2 = round2Cats.readline()
    counter1 = 1
    counter2 = 7
    while(item != ""):
        cat_plate = pygame.font.SysFont("arial",50)
        #remove the extra character at the end (that makes the box) - don't do for last item, because will lose a letter
        if(counter1 != 6):
            item = item[:-2]
        if(counter2 != 12):
            item2 = item2[:-2]
        #creates png's for each category header
        head1 = cat_plate.render(item, True, (195,174,46), (14,27,121))
        head2 = cat_plate.render(item2, True, (195,174,46), (14,27,121))
        image1 = pygame.transform.scale(head1,(120,95))
        image2 = pygame.transform.scale(head2,(120,95))
        pygame.image.save(image1, "cat"+str(counter1)+".png")
        pygame.image.save(image2, "cat"+str(counter2)+".png")
        item = round1Cats.readline()
        item2 = round2Cats.readline()
        counter1+=1
        counter2+=1
 
    #this loop reads in a category name and 5 questions for each round, then places them in lists to be
    #later given to box objects
    qSet1 = []
    qSet2 = []
    aSet1 = []
    aSet2 = []
    qSet1.append("placeholder")
    qSet2.append("placeholder")
    aSet1.append("placeholder")
    aSet2.append("placeholder")
    for i in xrange(30):
        qSet1.append(round1Qs.readline())
        aSet1.append(round1Qs.readline())
        qSet2.append(round2Qs.readline())
        aSet2.append(round2Qs.readline())
    round1Qs.close()
    round2Qs.close()

    #load the images into tuples of 3 to be fed to the box constructors
    images = [("done.png", "done.png", "done.png"), ("200.png", "400.png", "done.png"), ("400.png", "800.png", "done.png"),
              ("600.png", "1200.png", "done.png"), ("800.png", "1600.png", "done.png"),("1000.png", "2000.png", "done.png")]

    """Get the height and width of the screen, set the program to fill it"""
    size = width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode(size)
    """Set up x and y coordinates so as to center the game on the screen"""
    x = int((width - 910) / 2)
    y = int((height - 675) / 2)

    Menu(screen)
    nameA = user_input(screen, "Enter Team 1")
    nameB = user_input(screen, "Enter Team 2")
    nameC = user_input(screen, "Enter Team 3")

    """The box_counter gives the boxes numbers 1-36.  Two are chosen randomly as Daily Doubles."""
    box_counter = 1
    multiplier = 0
    counter = 1
    box = []
    """Create the box objects in batchse of 6 - to match categories. Multiplier is for assigning points depending upon round, the 2nd
    to last member (0-1000) is the base point value of that box"""
    for i in xrange(6):
        headers = ("cat"+str(i+1)+".png","cat"+str(i+7)+".png", "cat"+str(i+1)+".png")
        box.append(Box((qSet1[0], qSet1[0]), (aSet1[0], aSet2[0]), headers, x, y, multiplier, 0, box_counter))
        box_counter += 1
        box.append(Box((qSet1[i+counter], qSet2[i+counter]),(aSet1[i+counter], aSet2[i+counter]), images[1], x, y+100, multiplier, 200, box_counter))
        box_counter += 1 
        counter += 1
        box.append(Box((qSet1[i+counter], qSet2[i+counter]),(aSet1[i+counter], aSet2[i+counter]), images[2], x, y+200, multiplier, 400, box_counter))
        box_counter += 1  
        counter += 1
        box.append(Box((qSet1[i+counter], qSet2[i+counter]),(aSet1[i+counter], aSet2[i+counter]), images[3], x, y+300, multiplier, 600, box_counter))
        box_counter += 1  
        counter += 1
        box.append(Box((qSet1[i+counter], qSet2[i+counter]),(aSet1[i+counter], aSet2[i+counter]), images[4], x, y+400, multiplier, 800, box_counter))
        box_counter += 1 
        counter += 1
        box.append(Box((qSet1[i+counter], qSet2[i+counter]),(aSet1[i+counter], aSet2[i+counter]), images[5], x, y+500, multiplier, 1000, box_counter))
        box_counter += 1 
        x+=150
        multiplier +=1

    """shuffle the boxes so they appear randomly on the board"""
    boxes = random.shuffle(box)

    """create player objects"""
    names = [nameA, nameB, nameC]
    for i in xrange(3):
        player.append(Player(names[i]))
 
    gameBoard = Board(box, multiplier, player)
    """begin the game"""
    gameBoard.showBoard()
  
main()
    
