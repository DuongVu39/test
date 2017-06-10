class GameView:
    def __init__(self, image, screen):
        self.image = image
        self.screen = screen

    def draw(self, screen, gamemodel):
        #draw in pygame:
        pixel = 64
        # for y in range(self.map.height):
        #     for x in range(self.map.width):
        #         screen.blit(gamemodel, (gamemodel.x * pixel, gamemodel,y * pixel))

        screen.blit(self.image, (gamemodel.x, gamemodel.y))
