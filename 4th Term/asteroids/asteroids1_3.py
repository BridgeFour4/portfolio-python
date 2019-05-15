# asteroids 1.3
# nathan Broadbent

# imports
from superwires import games as game
import random
import math

# global variables
game.init(screen_width=1000, screen_height=750, fps=60)
SCORE = 0
LIVES = 3

# classes


class Asteroid(game.Sprite):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL: game.load_image("img/meteorsmall.png"),
              MEDIUM: game.load_image("img/meteormedium.png"),
              LARGE: game.load_image("img/meteor.png")}
    SPEED = 3
    SPAWN = random.randint(2, 4)

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

    def die(self):
        global SCORE
        SCORE += 100/self.size
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                a=Asteroid(x=self.x, y=self.y, size=self.size-1)
                game.screen.add(a)
        self.destroy()


class Ship(game.Sprite):
    ship_image = game.load_image("img/Spaceship.png")
    ROTATION_STEP = 7
    VELOCITY_STEP = .03
    MISSLE_DELAY = 25
    thruster_sound = game.load_sound("snd/thruster.wav")
    thruster_sound.set_volume(.05)

    def __init__(self):
        super(Ship, self).__init__(image=Ship.ship_image,
                                   x=game.screen.width / 2,
                                   y=game.screen.height / 2)
        self.missile_wait = 0

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
        if self.missile_wait > 0:
            self.missile_wait -= 1

        if game.keyboard.is_pressed(game.K_SPACE) and self.missile_wait == 0:
            shot = Laser(self.x, self.y, self.angle)
            game.screen.add(shot)
            self.missile_wait = Ship.MISSLE_DELAY
        # this is copied code look in better ways of doing it
        if self.left > game.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = game.screen.width
        if self.top > game.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = game.screen.height

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        self.destroy()



class Laser(game.Sprite):
    laser_image = game.load_image("img/laser.png")
    laser_sound = game.load_sound("snd/laser_shoot.wav")
    laser_sound.set_volume(.3)
    BUFFER = 60
    VELOCITY_FACTOR = 7
    LIFETIME = 40

    def __init__(self, ship_x, ship_y, ship_angle):
        Laser.laser_sound.play()
        angle = ship_angle*math.pi/180

        #calculate missle's starting position

        buffer_x = Laser.BUFFER*math.sin(angle)
        buffer_y = Laser.BUFFER*-math.cos(angle)

        x = ship_x + buffer_x
        y = ship_y + buffer_y
        dx = Laser.VELOCITY_FACTOR * math.sin(angle)
        dy = Laser.VELOCITY_FACTOR * -math.cos(angle)
        super(Laser, self).__init__(image=Laser.laser_image,
                                    x=x, y=y, dx=dx, dy=dy)
        self.lifetime = Laser.LIFETIME
        self.angle = ship_angle

    def update(self):
        if self.left > game.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = game.screen.width
        if self.top > game.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = game.screen.height
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()

        # check if missle overlaps another object on screen
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        self.destroy()


# main

def main():
    # load data
    background = game.load_image("img/space.png", transparent=False)

    # create objects
    ship = Ship()
    for i in range(8):
        asteroid = Asteroid(random.randrange(game.screen.width),
                            random.randrange(game.screen.height),
                            random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE]))
        game.screen.add(asteroid)

    # draw
    game.screen.background = background
    game.screen.add(ship)
    # game_setup

    # start loop
    game.screen.mainloop()

main()