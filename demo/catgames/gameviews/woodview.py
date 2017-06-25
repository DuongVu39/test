import  pygame
class WoodView:
    def __init__(self,image,screen):
        self.image = image
        self.screen = screen
        self.current_image = 0

    def draw(self,gamemodel, active):
        gamemodel.y += 2

        if gamemodel.y >= 0:
        #     self.current_image += 1
        #     if self.current_image > len(self.image):
        #         self.current_image = 0
            gamemodel.y = -600

        self.screen.blit (self.image, (gamemodel.x, gamemodel.y) )


