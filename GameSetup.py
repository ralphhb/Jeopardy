import pygame, Menu, Screen, Player, BoxLoader, Board

class GameSetup:
    def __init__(self, player, scr, screen):
        self.player = player
        self.screen = scr
        self.screen2 = screen
        self.boxes = []
        
    def setUpGame(self, gSetup):
        
        loader = BoxLoader.BoxLoader(self.screen2)
        self.boxes = loader.setupBoxes()
 
        board = Board.Board(self.player, self.screen)
        #self.setBoard(self.board)
        """begin the game"""
        board.showBoard(self.boxes, board)
        #self.answer = Answer.Answer(scr, self.players, self.board)

    def getBoard(self):
        return self.board

    def setBoard(self, board):
        self.board = board

    
