# apple Panic
# Created By Nathan Broadbent
# 4/19

# imports
from superwires import games, color
import random

# global Variables
games.init(screen_width=640, screen_height=480, fps=60)
LIVES = 3
SCORE = 0
lives_text = "LIVES: " + str(LIVES)
# classes


class Squirrel(games.Sprite):
    image = games.load_image("images/squirrel1.png")

    def __init__(self, y=60, speed=5, odds_change=100):
        super(Squirrel, self).__init__(image=Squirrel.image,
                                       x=games.screen.width/2,
                                       y=y,
                                       dx=speed)
        self.odds_change = odds_change
        self.time_til_drop = 0

    def update(self):
        if self.right > games.screen.width-30 or self.left < 30:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx
        self.check_drop()

    def check_drop(self):
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_apple = Apple(x=self.x, speed=random.randrange(Apple.speed)+1, speedx=random.randint(-3, 3))
            games.screen.add(new_apple)
            self.time_til_drop = random.randint(20, 100)


class Basket(games.Sprite):
    image = games.load_image("images/basket1.png")

    def __init__(self):
        super(Basket, self).__init__(image=Basket.image, x=games.mouse.x,
                                     bottom=games.screen.height)

    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.check_collide()

    def check_collide(self):
        global SCORE
        for apple in self.overlapping_sprites:
            # add to score()
            apple.handle_collide()
            if LIVES >= 0:
                SCORE += 10


class Apple(games.Sprite):
    image = games.load_image("images/apple1.png")
    speed = 10

    def __init__(self, x, y=90, speed=random.randrange(speed)+1, speedx=random.randint(-3, 3)):
        super(Apple, self).__init__(image=Apple.image, x=x, y=y, dy=speed, dx=speedx)

    def update(self):
        global LIVES
        if self.top > games.screen.height:
            self.destroy()
            LIVES -= 1
            if LIVES < 0:
                self.end_game()
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx

    def end_game(self):
        """end the game"""
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.green,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5*games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)

    def handle_collide(self):
        self.destroy()


class ScText(games.Text):
    def update(self):
        self.value = SCORE


class LivesText(games.Text):
    def update(self):
        global lives_text
        self.value = lives_text
        lives_text = "LIVES: " + str(LIVES)


# main
def main():
    # load Data
    bg_image = games.load_image("images/tree.png", transparent=False)

    # create objects
    basket = Basket()
    squirrel = Squirrel()
    score = ScText(value=SCORE, is_collideable=False, size=60, color=color.blue, x=550, y=30)
    lives = LivesText(value=lives_text, is_collideable=False, size=60, color=color.red, x=80, y=30)

    # draw
    games.screen.background = bg_image
    games.screen.add(basket)
    games.screen.add(squirrel)
    games.screen.add(score)
    games.screen.add(lives)

    # game setup
    games.mouse.is_visible = False
    games.screen.event_grab = True

    # start loop
    games.screen.mainloop()


# starting point
main()
