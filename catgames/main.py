from gamecontrollers.gamecontrollers import GameController
from gameviews.gameviews import GameView
from gameviews.catview import CatView
from gameviews.fishview import FishView
from gameviews.boneview import BoneView
from gamemodels.gamemodels import GameModel


import random
import pygame

pygame.init()
screen = pygame.display.set_mode((900, 600))
done = False


catmodel = GameModel(325, 400)
catmodel.move(50, 50)

groundmodel = GameModel(0, 0)
bonemodel = GameModel((random.randrange(225,650)),50)
fishmodel = GameModel((random.randrange(225,650)),50)

fish_list=[
    pygame.image.load("images/fish1.png"),
    pygame.image.load ( "images/fish2.png" ),
    pygame.image.load ( "images/fish3.png" ),
    pygame.image.load ( "images/fish4.png" )
]

cat_animations = [
    pygame.image.load("images/cat_right.png"),
    pygame.image.load("images/cat_left.png")
                    ]
catview = CatView(cat_animations, screen)
groundview = GameView(pygame.image.load("images/background.png"), screen)
fishview = FishView(random.choice(fish_list),screen)
boneview = BoneView(pygame.image.load("images/bone.png"),screen)

fish = GameController(fishmodel,fishview)
bone = GameController(bonemodel,boneview)
cat = GameController(catmodel, catview)
ground = GameController(groundmodel, groundview)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        cat.handle_input(event)
    ground.draw()
    bone.draw()
    fish.draw()
    cat.draw()
    pygame.display.flip()

