from gamecontrollers.gamecontrollers import GameController
from gameviews.gameviews import GameView
from gamemodels.gamemodel import GameModel


import pygame
pygame.init()
screen = pygame.display.set_mode((640, 640))
done = False

playermodel = GameModel(100, 200)
assert playermodel.x == 100, playermodel.y == 200
playermodel.move(10, 10)
assert playermodel.x == 110, playermodel.y == 210

groundmodel = GameModel(10, 40)
assert groundmodel.x == 10, groundmodel.y == 40


playerview = GameView(pygame.image.load("images/cat_left.png"), screen)
groundview = GameView(pygame.image.load("images/sea.jpg"), screen)
ground_image = pygame.image.load("images/Grass.png")

player = GameController(playermodel, playerview)
ground = GameController(groundmodel, groundview)

counter = 0


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        ground.draw(screen)
        player.handle_input(event)
        player.draw(screen)
        # screen.fill((0, 0, 0))
    # player.counter += 1
    # if player.counter >= 10:
    #     player.move(1, 0)
    #     player.counter = 0

    pygame.display.flip()