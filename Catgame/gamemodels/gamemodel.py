class GameModel:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    #
    # def collide
    #
    # def in_map
