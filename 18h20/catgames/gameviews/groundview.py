import  pygame
class GameView:
    def __init__(self,image,screen):
        self.image = image
        self.screen = screen

    def draw(self,gamemodel, active):

        self.screen.blit ( self.image, (gamemodel.x, gamemodel.y) )


    def check_map(y):
        if y < 225 or y > 600:
            return False
        return  True



