import random
class FishView:
    def __init__(self,images,screen):
        self.images = images
        self.screen = screen
        self.current_img = 0
        self.time = 20
        self.counter =0
    def draw(self,model):

        self.counter +=1
        if self.counter >=self.time:
            model.y += 2

        if model.y >= 900:
            model.y = 0
            model.x = random.randint(225,650)
        self.screen.blit(self.images, (model.x, model.y))