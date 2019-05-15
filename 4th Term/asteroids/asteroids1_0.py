# asteroids 1.0
# nathan Broadbent

# imports
from superwires import games as game
import random

# global variables
game.init(screen_width=640, screen_height=480, fps=60)

# classes

class Asteroid(game.Sprite):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL: game.load_image("img/meteorsmall.png"),
              MEDIUM: game.load_image("img/meteormedium.png"),
              LARGE: game.load_image("img/meteor.png")}
    SPEED = 3

    def __init__(self, x, y, size):
        super(Asteroid, self).__init__(image=Asteroid.images[size],
                                        x=x,
                                        y=y,
                                        dx=random.choice([1, -1]) * Asteroid.SPEED * random.random()/size,
                                        dy=random.choice([1, -1]) * Asteroid.SPEED * random.random() / size
                                       )
        self.size = size

    def update(self):
        if self.left > game.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = game.screen.width
        if self.top > game.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = game.screen.height

# main

def main():
    # load data
    background = game.load_image("img/space.png", transparent=False)

    # create objects
    for i in range(8):
        asteroid = Asteroid(random.randrange( game.screen.width),
                            random.randrange( game.screen.height),
                            random.choice([Asteroid.SMALL,Asteroid.MEDIUM,Asteroid.LARGE]))
        game.screen.add(asteroid)

    # draw
    game.screen.background = background



    # game_setup

    # start loop
    game.screen.mainloop()

main()