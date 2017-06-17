import   pygame
class CatView:
    def __init__(self, images, screen):
        self.images = images
        self.screen = screen
        self.current_img = 0
        self.time = 20
        self.counter =0
        self.width = 87
        self.height = 144

    def draw(self, model, active):
        self.counter +=1
        if self.counter >=self.time:
            self.current_img +=1
            if self.current_img >= len(self.images):
                self.current_img =0
            self.counter = 0
        self.screen.blit(self.images[self.current_img],(model.x,model.y))
