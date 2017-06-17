import  pygame
import random
fish_list=[
    pygame.image.load("images/fish1.png"),
    pygame.image.load ( "images/fish2.png" ),
    pygame.image.load ( "images/fish3.png" )

]
class GameController:
    def __init__(self, gamemodel, gameview):
        self.gamemodel = gamemodel
        self.gameview = gameview
        self.counter = 0
        self.active = True
        self.right_pressed = False
        self.left_pressed = False
        self.speed= 2
    def check_active(self):
        if self.active == False:
            t = random.randint(0,2)
            self.gameview.image = fish_list[t]
            self.active = True

    def draw(self):
        self.active = self.gameview.draw (self.gamemodel, self.active)
        self.check_active()

    def move(self, dx, dy):
        self.gamemodel.move ( dx, dy )

    def handle_input(self, event):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                self.right_pressed = True
            elif event.key == pygame.K_LEFT:
                self.left_pressed = True
            elif event.key == pygame.K_F5:
                pass

            elif event.key == pygame.K_ESCAPE:
                quit ()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.right_pressed = False
            elif event.key == pygame.K_LEFT:
                self.left_pressed = False


    def eat(self, food_list):
        for food in food_list:
            if self.gamemodel.collide(food, self.gameview):
                food.active = False
                food.gamemodel.revive()

    def dont_eat(self,bone):
        if self.gamemodel.collide ( bone, self.gameview ):
           bone.active = False
           bone.gamemodel.revive ()
           return  True

    def point_collide(self,food_list):
        for food in food_list:
            if self.gamemodel.collide(food, self.gameview):
                food.active = False
                return True
    def heath_collide(self,bones):
        if self.gamemodel.collide(bones,self.gameview):
            return  True
    def update(self, food):
        dx = 0
        dy = 0

        if self.right_pressed:
            dx += self.speed
        if self.left_pressed:
            dx -= self.speed
        self.move(dx * 2, dy * 2)
        self.eat(food)

    #     if self.current_level < level:
    #         self.current_level = level
    #         self.gameview.time -= 5
