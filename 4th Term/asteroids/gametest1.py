# Frozen Jam by tgfcoder <https://twitter.com/tgfcoder> licensed under CC-BY-3
# Read key
# Demonstartes reading the keyboard

from superwires import games

games.init(screen_width=640, screen_height = 480, fps= 50)


class Ship(games.Sprite):
    ship_image = games.load_image("img/Spaceship.png")

    def __init__(self):
        super(Ship, self).__init__(image=Ship.ship_image,
                                   x=games.screen.width/2,
                                   y=games.screen.height/2)
    def update(self):
        if games.keyboard.is_pressed(games.K_w) or games.keyboard.is_pressed(games.K_UP):
            self.y -= 10
        if games.keyboard.is_pressed(games.K_s)or games.keyboard.is_pressed(games.K_DOWN):
            self.y += 10
        if games.keyboard.is_pressed(games.K_a)or games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= 10
        if games.keyboard.is_pressed(games.K_d)or games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += 10

        if games.keyboard.is_pressed(games.K_1):
            self.angle = 0
        if games.keyboard.is_pressed(games.K_2):
            self.angle = 90
        if games.keyboard.is_pressed(games.K_3):
            self.angle = 180
        if games.keyboard.is_pressed(games.K_4):
            self.angle = 270

        if self.left > games.screen.width:
            self.right = 0
        if self.right < 0:
            self.left = games.screen.width
        if self.top > games.screen.height:
            self.bottom = 0
        if self.bottom < 0:
            self.top = games.screen.height



def main():

    # load data
    background = games.load_image("img/space.png", transparent=False)
    explosion_files = ["img/explosion1.png",
                       "img/explosion2.png",
                       "img/explosion3.png",
                       "img/explosion4.png",
                       "img/explosion5.png"]

    #laser_sound = games.load_sound("snd/laser_Shoot.wav")
    #games.music.load("snd/tgfcoder-FrozenJam-SeamlessLoop.ogg")

    # create objects
    the_ship = Ship()
    explosion = games.Animation(images=explosion_files,
                                x=games.screen.width/2,
                                y=games.screen.height/2,
                                n_repeats=1,
                                repeat_interval=5)

    # draw
    games.screen.background = background
    games.screen.add(the_ship)
    games.screen.add(explosion)

    # game_setup

    # start loop
    games.screen.mainloop()


main()
