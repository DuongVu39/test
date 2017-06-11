from gamecontrollers.gamecontrollers import GameController
from gameviews.gameviews import GameView
from gameviews.catview import CatView
from gamemodels.gamemodel import GameModel



import pygame
pygame.init()
screen = pygame.display.set_mode((648, 480))
done = False

catmodel = GameModel(100, 200)
assert catmodel.x == 100, catmodel.y == 200
catmodel.move(10, 10)
assert catmodel.x == 110, catmodel.y == 210

groundmodel = GameModel(10, 40)
assert groundmodel.x == 10, groundmodel.y == 40

cat_animations = [
    pygame.image.load("images/cat_right.png"),
    pygame.image.load("images/cat_left.png")
                    ]
catview = CatView(cat_animations, screen)
groundview = GameView(pygame.image.load("images/sea.jpg"), screen)
ground_image = pygame.image.load("images/Grass.png")

cat = GameController(catmodel, catview)
ground = GameController(groundmodel, groundview)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        cat.handle_input(event)
    ground.draw()

    cat.draw()
        # screen.fill((0, 100, 0))


    pygame.display.flip()