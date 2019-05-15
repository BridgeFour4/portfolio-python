from superwires import games

games.init(screen_width=640, screen_height = 480, fps= 50)
laser_sound = games.load_sound("snd/laser_Shoot.wav")
games.music.load("snd/tgfcoder-FrozenJam-SeamlessLoop.ogg")


choice = None
while choice !=0:

    print(
        """
        Sound and Music
        0-quit
        1- play missle sound
        2- loop missle sound
        3- stop missle sound
        4 play theme
        5- loop theme
        6 stop theme
        """
    )

    choice = input("Choice:")
    print()

    if choice == "0":
        print("Goodbye")
    if choice == "1":
        laser_sound.play()
    if choice == "2":
        loop = input("how many loops (-1=forever)")
        laser_sound.play(loop)
    if choice == "3":
        laser_sound.stop()

    if choice == "4":
        games.music.play()
    if choice == "5":
        loop = input("how many loops (-1=forever)")
        games.music.play(loop)
    if choice == "6":
        games.music.stop()


