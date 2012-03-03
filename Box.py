class Box:
    """The box object holds it's coordinates, images and questions for both rounds. Mulitplyer is used to set the coordinates
    isClicked checks. It will have a value of 0-5. """
    def __init__(self, question, answer, images, x, y, multiplier, pointValue, box_counter):
        self.x = x
        self.y = y
        self.question1 = question[0]
        self.question2 = question[1]
        self.answer1 = answer[0]
        self.answer2 = answer[1]
        self.image = images[0]
        self.doubleJImage = images[1]
        self.doneImage = images[2]
        self.pointValue = pointValue
        self.beenClicked = False
  
        #Cut the extra box character off the questions and answers
        #self.question1 = self.question1[:-2]
        #self.question2 = self.question2[:-2]
        #self.answer1 = self.answer1[:-2]
        #self.answer2 = self.answer2[:-2]

    def getImage(self, doubleJeopardy):
        if self.beenClicked == True:
            return self.doneImage
        elif doubleJeopardy:
            return self.doubleJImage
        else:
            return self.image

    def getQuestion(self, doubleJeopardy):
        if doubleJeopardy:
            return self.question2
        else:
            return self.question1
        
    def getAnswer(self, doubleJeopardy):
        if doubleJeopardy:
            return self.answer2
        else:
            return self.answer1
    
    def getCoords(self):
        return (self.x, self.y)

    def setFrame(self, frame):
        self.frame = frame

    def getFrame(self):
        return self.frame

    def getPoints(self, doubleJeopardy):
        if doubleJeopardy:
            return self.pointValue * 2
        return self.pointValue
   
                
    def setBeenClicked(self):
        if self.beenClicked:
            self.beenClicked = False
        else:
            self.beenClicked = True

    def getBeenClicked(self):
        return self.beenClicked

    def getDailyDoubleID(self):
        return self.daily_double_id

    def setDailyDouble(self, num):
        self.daily_double = num
