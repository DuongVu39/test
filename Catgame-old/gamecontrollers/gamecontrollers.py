import pygame
from gameviews.gameviews import GameView


class GameController:
    def __init__(self, gamemodel, gameview):
        self.gamemodel = gamemodel
        self.gameview = gameview
        self.counter = 0

    def draw(self):
        self.gameview.draw(self.gamemodel)

    def move(self, dx, dy):
        self.gamemodel.move(dx, dy)


    def handle_input(self, event):
        dx = 0
        dy = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print(11)
                dy -= 1
            elif event.key == pygame.K_DOWN:
                dy += 1
            elif event.key == pygame.K_RIGHT:
                dx += 1
            elif event.key == pygame.K_LEFT:
                dx -= 1
            elif event.key == pygame.K_ESCAPE:
                quit()
        print(dx, dy)
        self.move(dx * 10,dy * 10)
        print(self.gamemodel.x, self.gamemodel.y)


        # if self.cat.collide(self.box, dx, dy):
        #     if self.in_map(self.box, dx, dy):
        #         self.box.move(dx, dy)
        #         self.pusher.move(dx, dy)
        # elif self.in_map(self.pusher, dx, dy):
        #     self.pusher.move(dx, dy)
        # elif self.box.check_win(self.dest):
        #     self.draw_image_center(screen, win_image)
        #     time.sleep(10)
        #     quit()
