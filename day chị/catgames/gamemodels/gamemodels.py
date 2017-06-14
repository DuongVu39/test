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

    def point_collide(self, x, y, object):
        pass

    def collide(self, itemcontroller, catview):
        item = itemcontroller.gamemodel
        item_view = itemcontroller.gameview


        if (item.x <= self.x+catview.width & item.x +item_view.width >= self.x & item.y <= self.y + catview.height & item.y+ item_view.height>= self.y  ):

        # if  (item.x <= self.x <=  item.x + item_view.width) and (item.y <= self.y <=  item.y + item_view.height):
        #     return True
        #
        # elif (item.x <= self.x + catview.width <=  item.x + item_view.width) and  (item.y <= self.y <=  item.y + item_view.height):
        #     return  True
        #
        # elif (item.x <= self.x + catview.width <=  item.x + item_view.width) and  (item.y <= self.y + catview.height <=  item.y + item_view.height):
        #     return  True
        #
        # elif (item.x <= self.x <=  item.x + item_view.width) and  (item.y <= self.y + catview.height <=  item.y + item_view.height):
            return True

        else:
            return  False

    def revive(self):
        self.y = 0
        self.x = random.randint ( 225, 600 )