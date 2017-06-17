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
myfont = pygame.font.SysFont("monospace",20)

catmodel = GameModel(325, 400)
catmodel.move(50, 50)

groundmodel = GameModel(0, 0)
bonemodel = GameModel((random.randrange(225,600)),50)
fishmodel = GameModel((random.randrange(225,600)),50)

fish_list=[
    pygame.image.load("images/fish1.png"),
    pygame.image.load ( "images/fish2.png" ),
    pygame.image.load ( "images/fish3.png" )

]

cat_animations = [
    pygame.image.load("images/catleft1.png"),
    pygame.image.load("images/catright1.png"),

                    ]
catview = CatView(cat_animations, screen)
groundview = GameView(pygame.image.load("images/background.png"), screen)
fishview = FishView ( random.choice ( fish_list ), screen )
boneview = BoneView(pygame.image.load("images/bone.png"),screen)

fish = GameController(fishmodel,fishview)
fish_s = [fish]
fish_s.append(GameController(GameModel((random.randrange(225,600)),-50), FishView ( random.choice ( fish_list ), screen )))
fish_s.append(GameController(GameModel((random.randrange(225,600)),-100), FishView ( random.choice ( fish_list ), screen )))

bone = GameController(bonemodel,boneview)
cat = GameController(catmodel, catview)
ground = GameController(groundmodel, groundview)
food = [fish for fish in fish_s]
food.append(bone)
# catmodel.dead = False
score=0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        cat.handle_input(event)


    ground.draw()

    bone.draw()
    for fish in fish_s:
        fish.draw()

    if cat.point_collide(food) == True:
        score +=1
    if catmodel.check_dead () == False:
        cat.update(food)
        cat.draw ()
    else:
        score_text = pygame.font._SysFont("monospace",100).render("YOU LOSE",1,(255,255,0))
        screen.blit(score_text,)
    score_text = myfont.render("Score = "+ str(score),1,(0,0,0))
    screen.blit(score_text,(1,1))




    pygame.display.flip()

