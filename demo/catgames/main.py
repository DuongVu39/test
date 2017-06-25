from gamecontrollers.gamecontrollers import GameController
from gameviews.groundview import GameView
from gameviews.woodview import WoodView
from gameviews.catview import CatView
from gameviews.fishview import FishView
from gameviews.boneview import BoneView
from gamemodels.gamemodels import GameModel
from gameviews.sharkview import SharkView
from gameviews.upview import UpView

import random
import pygame
pygame.init()



sound_bone= pygame.mixer.Sound("music/bone.wav")
sound_end = pygame.mixer.Sound("music/end.wav" )
sound_eat = pygame.mixer.Sound( "music/eat.wav" )
pygame.mixer.music.load("music/bg_music.mp3")
pygame.mixer.music.play(-1)


screen = pygame.display.set_mode((900, 600))
done = False
myfont = pygame.font.SysFont("monospace",20,bold=True)
speed = 3

catmodel = GameModel(325, 400)
catmodel.move(50, 50)

groundmodel = GameModel(0, 0)
woodmodel = GameModel(222, -600)
bonemodel = GameModel((random.randrange(225,600)),50)
fishmodel = GameModel((random.randrange(225,600)),50)
sharkmodel= GameModel((random.randrange(225,600)),50)
upmodel= GameModel(0,200)
fish_list=[
    pygame.image.load("images/fish1.png"),
    pygame.image.load ( "images/fish2.png" ),
    pygame.image.load ( "images/fish3.png" )

]
sharklist=[
    pygame.image.load("images/shark.png"),
    pygame.image.load("images/shark2.png")
]

cat_animations = [
    pygame.image.load("images/catleft.png"),
    pygame.image.load("images/catright.png"),
                 ]
sharkview = SharkView(random.choice(sharklist),screen)
catview = CatView(cat_animations, screen)
groundview = GameView(pygame.image.load("images/background.png"), screen)
fishview = FishView ( random.choice ( fish_list ), screen )
boneview = BoneView(pygame.image.load("images/bone.png"),screen)
woodview = WoodView(pygame.image.load("images/wood.png"), screen)


fish = GameController(fishmodel,fishview)
fish_s = [fish]
fish_s.append(GameController(GameModel((random.randrange(225,600)),-50), FishView ( random.choice ( fish_list ), screen )))
fish_s.append(GameController(GameModel((random.randrange(225,600)),-100), FishView ( random.choice ( fish_list ), screen )))

shark = GameController(sharkmodel,sharkview)
bone = GameController(bonemodel,boneview)
cat = GameController(catmodel, catview)
ground = GameController(groundmodel, groundview)
wood = GameController(woodmodel, woodview)
food = [fish for fish in fish_s]


health=5

score=0
level = 1
level_current = 1
text_time = 3
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        cat.handle_input(event)

    ground.draw()
    wood.draw()
    bone.draw()
    for fish in fish_s:
        fish.draw()


    if cat.dont_eat(bone)==True:
        health-=1
        sound_bone.play ()
        cat.dont_eat(bone) == False



    if catmodel.check_dead () == False and health > 0:
        if cat.point_collide ( food ) == True:
            sound_eat.play ()
        score = cat.eat ( food )

        cat.update(food)
        cat.draw ()

    else:

        health = 0

        sound_eat.stop()
        sound_bone.stop()
        pygame.mixer.music.stop()
        sound_end.play ()
        ground.draw ()
        wood.draw ()
        score_text = pygame.font.SysFont ( "monospace", 100 ).render ( "YOU LOSE", 1, (255, 255, 0) )
        screen.blit ( score_text, (210, 200) )
        score_text = pygame.font.SysFont ( "monospace", 50 ).render ( "YOUR SCORE: "+ str(score), 1, (255, 255, 0) )
        screen.blit ( score_text, (250, 300) )


    score_text = myfont.render("Score: "+ str(score),1,(0,100,0))
    screen.blit(score_text,(10,1))

    level_text = myfont.render ("Level: " + str ( level), 1, (0, 100, 0) )
    screen.blit(level_text,(10,20))

    heath_text = myfont.render("Health: "+str(health),1,(0,100,0))
    screen.blit(heath_text,(10,40))

    target_score = 10*level_current


    if level == level_current and score == target_score:

        for fish in fish_s:
            fish.gameview.speed += 0.5
            fish.draw ()
        bone.gameview.speed += 0.5
        cat.speed += 0.5
        level_current += 1
        level += 1





    if level >= 3:
        shark.draw ()
        if cat.dont_eat( shark ) == True:
            health-=3


    pygame.display.flip()

