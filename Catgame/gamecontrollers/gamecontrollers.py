import pygame
class GameController:
    def __init__(self, gamemodel, gameview):
        self.gamemodel = gamemodel
        self.gameview = gameview
        self.counter = 0

    def draw(self, screen):
        self.gameview.draw(screen, self.gamemodel)

    def move(self, dx, dy):
        self.gamemodel.move(dx, dy)

    def handle_input(self, event):
        dx = 0
        dy = 0
        # saved_pusher = self.pusher.copy()
        # saved_boxes = self.box.copy()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy -= 1
            elif event.key == pygame.K_DOWN:
                dy += 1
            elif event.key == pygame.K_RIGHT:
                dx += 1
            elif event.key == pygame.K_LEFT:
                dx -= 1
            elif event.key == pygame.K_ESCAPE:
                quit()
