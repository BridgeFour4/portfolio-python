# asteroids 1.3
# nathan Broadbent

# imports
from superwires import color, games
import random
import math

# global variables
games.init(screen_width=1000, screen_height=750, fps=60)


# classes


class Game(object):
    def __init__(self):
        self.level = 0
        self.sound = games.load_sound("snd/level.wav")
        self.lives = games.Text(value=3,
                  size=50,
                  color=color.red,
                  top=5,
                  right=50,
                  is_collideable=False)
        self.score = games.Text(value=0,
                  size=30,
                  color=color.white,
                  top=5,
                  right=games.screen.width - 10,
                  is_collideable=False)
        self.ufoscore = 1000
        games.screen.add(self.score)
        games.screen.add(self.lives)
        self.player = Ship(self,games.screen.width/2, games.screen.height/2)
        games.screen.add(self.player)


    def run(self):
        self.start()
        games.music.load('snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
        games.music.play(-1)
        background = games.load_image("img/space.png", transparent=False)
        games.screen.background = background
        self.advance()
        games.screen.mainloop()

    def advance(self):
        self.sound.play()
        self.level += 1
        BUFFER = 150
        for i in range(self.level):
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min

            x_distance = random.randrange(x_min, games.screen.width-x_min)
            y_distance = random.randrange(y_min, games.screen.width - y_min)

            x = self.player.x + x_distance
            y = self.player.y + y_distance

            # wrap around screen if escesary
            x %= games.screen.width
            y %= games.screen.height
            asteroid = Asteroid(self,
                                x,
                                y,
                                Asteroid.LARGE)
            games.screen.add(asteroid)

            level_message = games.Message(value = "level"+str(self.level),
                                          size = 40,
                                           color = color.yellow,
                                          x= games.screen.width/2,
                                          y = games.screen.width/10,
                                          lifetime=3* games.screen.fps,
                                          is_collideable = False)
            games.screen.add(level_message)

    def start(self):
        start_message = games.Message(value="Asteroids",
                                    size=90,
                                    color=color.white,
                                    x=games.screen.width/2,
                                    y=games.screen.height/4,
                                    lifetime=3*games.screen.fps,
                                    is_collideable=False)
        start_message2 = games.Message(value="use arrow keys to move and space to shoot and",
                                      size=40,
                                      color=color.white,
                                      x=games.screen.width / 2,
                                      y=games.screen.height / 2,
                                      lifetime=3 * games.screen.fps,
                                      is_collideable=False)
        start_message3 = games.Message(value="try to navigate your way out of the asteroid field ",
                                       size=40,
                                       color=color.white,
                                       x=games.screen.width / 2,
                                       y=games.screen.height / 2+100,
                                       lifetime=3 * games.screen.fps,
                                       is_collideable=False)
        games.screen.add(start_message)
        games.screen.add(start_message2)
        games.screen.add(start_message3)
    def end(self):
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5*games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
        games.screen.add(end_message)

    def respawn(self):
        self.player = Ship(self, x=games.screen.width/2, y=games.screen.height/2)
        games.screen.add(self.player)

    def ufocheck(self):
        if self.score.value >=self.ufoscore:
            self.ufoscore+=self.score.value
            ufo = Ufo(self,self.player)
            games.screen.add(ufo)



class Wrapper(games.Sprite):
    def update(self):
        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height

    def die(self):
        self.destroy()


class Collider(Wrapper):
    def update(self):
        super(Collider, self).update()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        # create explosion
        explosion = Explosion(self.x,self.y)
        # add explosion to screen
        games.screen.add(explosion)
        self.destroy()


class Asteroid(Wrapper):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL: games.load_image("img/meteorsmall.png"),
              MEDIUM: games.load_image("img/meteormedium.png"),
              LARGE: games.load_image("img/meteor.png")}
    SPEED = 3
    SPAWN = random.randint(2, 4)
    POINTS = 100
    TOTAL = 0

    def __init__(self, game, x, y, size):
        Asteroid.TOTAL += 1
        super(Asteroid, self).__init__(image=Asteroid.images[size],
                                       x=x,
                                       y=y,
                                       dx=random.choice([1, -1]) * Asteroid.SPEED * random.random()/size,
                                       dy=random.choice([1, -1]) * Asteroid.SPEED * random.random() / size
                                       )
        self.size = size
        self.game = game

    def die(self):
        Asteroid.TOTAL -= 1
        self.game.score.value += Asteroid.POINTS//self.size
        self.game.score.right = games.screen.width-10
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                a = Asteroid(self.game, x=self.x, y=self.y, size=self.size-1)
                games.screen.add(a)
        if Asteroid.TOTAL == 0:
            self.game.advance()
        self.game.ufocheck()
        super(Asteroid, self).die()


class Ship(Collider):
    ship_image = games.load_image("img/Spaceship.png")
    ROTATION_STEP = 7
    VELOCITY_STEP = .03
    MISSLE_DELAY = 25
    VELOCITY_MAX = 3
    thruster_sound = games.load_sound("snd/thruster.wav")
    thruster_sound.set_volume(.05)

    def __init__(self,game,x,y):
        super(Ship, self).__init__(image=Ship.ship_image,
                                   x=x,
                                   y=y)
        self.missile_wait = 0
        self.game = game

    def update(self):
        super(Ship, self).update()
        if games.keyboard.is_pressed(games.K_a)or games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_d)or games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_w) or games.keyboard.is_pressed(games.K_UP):
            Ship.thruster_sound.play()
            angle = self.angle * math.pi/180
            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)
            self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
            self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)

        if self.missile_wait > 0:
            self.missile_wait -= 1

        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            shot = Laser(self.x, self.y, self.angle)
            games.screen.add(shot)
            self.missile_wait = Ship.MISSLE_DELAY

    def die(self):
        self.game.lives.value -= 1
        if self.game.lives.value == 0:
            self.game.end()
        else:
            self.game.respawn()
        super(Ship, self).die()


class Laser(Collider):
    laser_image = games.load_image("img/laser.png")
    laser_sound = games.load_sound("snd/laser_shoot.wav")
    laser_sound.set_volume(.3)
    BUFFER = 60
    VELOCITY_FACTOR = 7
    LIFETIME = 40

    def __init__(self, ship_x, ship_y, ship_angle):
        Laser.laser_sound.play()
        angle = ship_angle*math.pi/180

        # calculate missle's starting position

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
        super(Laser, self).update()
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()


class Ufo(Collider):
    ship_image = games.load_image("img/Spaceship.png")
    def __init__(self,game,player):
        super(Ufo, self).__init__(image=Ship.ship_image,
                                   x=games.screen.width,
                                   y=0,
                                   dx=-2,
                                   dy=2)
        self.missile_wait = 120
        self.game = game
        self.player = player
        self.angle = 225

    def update(self):
        if self.right < 0:
            self.destroy()
        self.missile_wait -= 1
        if self.missile_wait == 0:
            self.missile_wait = 120
            self.shoot()


    def shoot(self):
        if self.player.x < self.x and self.player.y < self.y:
            self.angle = random.randint(270, 360)
        if self.player.x < self.x and self.player.y > self.y:
            self.angle = random.randint(180, 270)
        if self.player.x > self.x and self.player.y < self.y:
            self.angle = random.randint(0, 90)
        if self.player.x > self.x and self.player.y > self.y:
            self.angle = random.randint(90, 180)
        shot = Laser(self.x, self.y, self.angle)
        games.screen.add(shot)

    def die(self):
        self.game.score.value += 500
        self.game.ufocheck()
        Wrapper.die(self)


class Explosion(games.Animation):
    images = ["img/explosion1.png",
              "img/explosion2.png",
              "img/explosion3.png",
              "img/explosion4.png",
              "img/explosion5.png"]
    sound = games.load_sound("snd/explosion3.wav")
    def __init__(self,x,y):
        super(Explosion, self).__init__(images=Explosion.images,
                                        x=x,
                                        y=y,
                                        n_repeats=1,
                                        repeat_interval=5,
                                        is_collideable=False)
        Explosion.sound.play()


# main

def main():
   g = Game()
   g.run()


main()
