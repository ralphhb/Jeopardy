import random

class DailyDoubleSetter:
    def __init__(self, box):
        self.counter = 0
        self.pickedBox = 0
        self.box = box
    
    """Sets which boxes are daily doubles, 1 for the first round and two for the second"""
    def setDailyDoubles(self):
        dd = random.randrange(36)
        self.counter+=1

        while self.box[dd].getQuestion == "placeholder" or dd == self.pickedBox:
            dd = random.randrange(36)
        if self.counter == 2:
            self.pickedBox == dd
        return dd


    
    

