import pygame, Box, random

class BoxLoader:
    def __init__(self, screen):
        self.images = [("done.png", "done.png", "done.png"), ("200.png", "400.png", "done.png"), ("400.png", "800.png", "done.png"),
              ("600.png", "1200.png", "done.png"), ("800.png", "1600.png", "done.png"),("1000.png", "2000.png", "done.png")]
        self.box_counter = 1
        self.multiplier = 0
        self.counter = 1
        self.box = []
        self.screen = screen
        self.qSet1 = []
        self.qSet2 = []
        self.aSet1 = []
        self.aSet2 = []
        self.qSet1.append("placeholder")
        self.qSet2.append("placeholder")
        self.aSet1.append("placeholder")
        self.aSet2.append("placeholder")
        for i in xrange(30):
            self.qSet1.append("blah"+ str(i)+"")
            self.qSet2.append("woo"+ str(i)+"")
            self.aSet1.append("blah"+ str(i)+"")
            self.aSet2.append("hoo"+ str(i)+"")
    
    """The box_counter gives the boxes numbers 1-36.  Two are chosen randomly as Daily Doubles."""

    """Create the box objects in batchse of 6 - to match categories. Multiplier is for assigning points depending upon round, the 2nd
    to last member (0-1000) is the base point value of that box"""
    def setupBoxes(self):
        x = self.screen.getX()
        y = self.screen.getY()
        for i in xrange(6):
            headers = ("cat"+str(i+1)+".png","cat"+str(i+7)+".png", "cat"+str(i+1)+".png")
            self.box.append(Box.Box((self.qSet1[0], self.qSet1[0]), (self.aSet1[0], self.aSet2[0]), headers, x, y, self.multiplier, 0, self.box_counter))
            self.box_counter += 1
            self.box.append(Box.Box((self.qSet1[i+self.counter], self.qSet2[i+self.counter]),(self.aSet1[i+self.counter], self.aSet2[i+self.counter]), self.images[1], x, y+100, self.multiplier, 200, self.box_counter))
            self.box_counter += 1 
            self.counter += 1
            self.box.append(Box.Box((self.qSet1[i+self.counter], self.qSet2[i+self.counter]),(self.aSet1[i+self.counter], self.aSet2[i+self.counter]), self.images[2], x, y+200, self.multiplier, 400, self.box_counter))
            self.box_counter += 1  
            self.counter += 1
            self.box.append(Box.Box((self.qSet1[i+self.counter], self.qSet2[i+self.counter]),(self.aSet1[i+self.counter], self.aSet2[i+self.counter]), self.images[3], x, y+300, self.multiplier, 600, self.box_counter))
            self.box_counter += 1  
            self.counter += 1
            self.box.append(Box.Box((self.qSet1[i+self.counter], self.qSet2[i+self.counter]),(self.aSet1[i+self.counter], self.aSet2[i+self.counter]), self.images[4], x, y+400, self.multiplier, 800, self.box_counter))
            self.box_counter += 1 
            self.counter += 1
            self.box.append(Box.Box((self.qSet1[i+self.counter], self.qSet2[i+self.counter]),(self.aSet1[i+self.counter], self.aSet2[i+self.counter]), self.images[5], x, y+500, self.multiplier, 1000, self.box_counter))
            self.box_counter += 1 
            x+=150
            self.multiplier +=1

        """shuffle the boxes so they appear randomly on the board"""
        random.shuffle(self.box)
        return self.box
