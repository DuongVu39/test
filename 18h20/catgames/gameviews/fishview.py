import random,pygame
class FishView:
    def __init__(self,image,screen):
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.screen = screen
        self.current_img = 0
        self.time = 20
        self.counter =0
        self.speed = 4


    def draw(self, model, active):
        self.counter +=1
        if self.counter >=self.time:
            model.y += self.speed

        if model.y >= 900:
            model.y = 0
            model.x = random.randint(225,600)
            active = False

        if active :
            self.screen.blit(self.image, (model.x, model.y))
        return active