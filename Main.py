import pygame, GameSetup, Screen, Menu, Player

def main():
    pygame.init()
    ####screen must return Screen object
    ####boxLoader must return boxes List
    screen = Screen.Screen()
    scr = screen.getScreen()
    menu = Menu.Menu(scr)
    #menu.startMenu()
    
    #nameA = menu.user_input(screen, "Enter Team 1")
    #nameB = menu.user_input(screen, "Enter Team 2")
    #nameC = menu.user_input(screen, "Enter Team 3")
    #names = [nameA, nameB, nameC]
    names = ["Andrei", "Natasha", "Dolokov"]
        
    """create player objects"""
    player = []
    for i in xrange(3):
        player.append(Player.Player(names[i]))
    g = GameSetup.GameSetup(player, scr, screen)
    g.setUpGame(g)
    
  
main()
