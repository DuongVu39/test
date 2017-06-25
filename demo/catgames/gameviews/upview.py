import random,pygame
class UpView:
    def __init__(self,images,screen):
        self.images = images
        self.width = 64
        self.height = 64
        self.screen = screen
        self.current_img = 0
        self.time = 10
        self.counter =0
        self.speed = 4
    def reset(self,model):
        model.x =0
    def draw(self,model, active):

        self.counter +=1

        if self.counter >=self.time:
            model.x += self.speed

        if model.x >= 900:
            active== False

        if active:
            self.screen.blit ( self.images, (model.x, 200) )
        return active


