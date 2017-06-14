from gamecontrollers.gamecontrollers import GameController
from gameviews.groundview import GameView
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
bonemodel = GameModel((random.randrange(225,600)),50)
fishmodel = GameModel((random.randrange(225,600)),50)

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
fishview = FishView ( random.choice ( fish_list ), screen )
boneview = BoneView(pygame.image.load("images/bone.png"),screen)

fish = GameController(fishmodel,fishview)
fish_sonhieu = [fish]
fish_sonhieu.append(GameController(GameModel((random.randrange(225,600)),200), FishView ( random.choice ( fish_list ), screen )))
bone = GameController(bonemodel,boneview)
cat = GameController(catmodel, catview)
ground = GameController(groundmodel, groundview)

food = [fish for fish in fish_sonhieu]
food.append(bone)
# catmodel.dead = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        cat.handle_input(event)


    ground.draw()
    bone.draw()
    for fish in fish_sonhieu:
        fish.draw()
# if catmodel.check_dead() == False:
    cat.update(food)
    cat.draw ()
    # if catmodel.collide(fishmodel, catview) == True:
    #     print("vao")




    pygame.display.flip()

