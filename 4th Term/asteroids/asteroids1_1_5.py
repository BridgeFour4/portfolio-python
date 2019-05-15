# asteroids 1.1.5
# nathan Broadbent

# imports
from superwires import games as game
import random
import math

# global variables
game.init(screen_width=1000, screen_height=750, fps=60)

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


class Ship(game.Sprite):
    ship_image = game.load_image("img/Spaceship.png")
    ROTATION_STEP = 7
    VELOCITY_STEP = .03
    thruster_sound = game.load_sound("snd/thrusters.wav")
    thruster_sound.set_volume(.5)

    def __init__(self):
        super(Ship, self).__init__(image=Ship.ship_image,
                                   x=game.screen.width / 2,
                                   y=game.screen.height / 2)

    def update(self):
        if game.keyboard.is_pressed(game.K_a)or game.keyboard.is_pressed(game.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if game.keyboard.is_pressed(game.K_d)or game.keyboard.is_pressed(game.K_RIGHT):
            self.angle += Ship.ROTATION_STEP
        if game.keyboard.is_pressed(game.K_w) or game.keyboard.is_pressed(game.K_UP):
            Ship.thruster_sound.play()
            angle = self.angle * math.pi/180
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)
        # this is copied code look in better ways of doing it
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
    ship = Ship()
    for i in range(8):
        asteroid = Asteroid(random.randrange( game.screen.width),
                            random.randrange( game.screen.height),
                            random.choice([Asteroid.SMALL,Asteroid.MEDIUM,Asteroid.LARGE]))
        game.screen.add(asteroid)

    # draw
    game.screen.background = background
    game.screen.add(ship)



    # game_setup

    # start loop
    game.screen.mainloop()

main()