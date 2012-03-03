####screen must return Screen object
    ####boxLoader must return boxes List
    scr = Screen.Screen()
    screen = scr.getScreen()
    menu = Menu.Menu(screen)
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
    loader = BoxLoader.BoxLoader(scr)
    boxes = loader.setupBoxes()
 
    gameBoard = Board.Board(player, screen)
    """begin the game"""
    gameBoard.showBoard(boxes)
