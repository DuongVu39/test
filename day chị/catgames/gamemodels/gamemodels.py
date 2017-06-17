import  pygame
import random
class GameModel:
    def __init__(self,x,y):
        self.x = x
        self.y = y

        self.dead = False
    def move(self,dx,dy):
        self.x += dx
        self.y += dy

    def check_dead(self):
        if self.x <225 or self.x > 600:
            self.dead = True
        return self.dead

<<<<<<< HEAD
=======


>>>>>>> ebdd7d6d9077bdf2070e44c33cfdb88f12f13017
    def collide(self, itemcontroller, catview):
        item = itemcontroller.gamemodel
        item_view = itemcontroller.gameview

<<<<<<< HEAD
        if (item.x <= self.x + catview.width) and (item.x + item_view.width >= self.x) and (item.y <= self.y + catview.height) and (item.y + item_view.height>= self.y):
=======

        if (item.x <= self.x +catview.width) and (item.x +item_view.width >= self.x) and (item.y <= self.y + catview.height) and (item.y+ item_view.height >= self.y ):
>>>>>>> ebdd7d6d9077bdf2070e44c33cfdb88f12f13017
            return True
        else:
            return  False

    # def point_collide(self, food_list):
    #     for food in food_list:
    #         if self.gamemodel.collide(food, self.gameview):
    #             return True

    def revive(self):
        self.y = 0
        self.x = random.randint ( 225, 600 )