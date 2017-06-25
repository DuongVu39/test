import random,pygame
class BoneView:
    def __init__(self,images,screen):
        self.images = images
        self.width = 64
        self.height = 64
        self.screen = screen
        self.current_img = 0
        self.time = 10
        self.counter =0
        self.speed = 3
    def draw(self,model, active):

        self.counter +=1
        if self.counter >=self.time:
            model.y += self.speed

        if model.y >= 600:
            model.y = 0
            model.x = random.randint(225,600)

        self.screen.blit(self.images,(model.x,model.y))