#nathan Broadbent
#10/18
import random
from asciiart import *
attack=0
secret=""
kraken=""


def askQuestion(question="default question", option1="", option2="", option3="",var=""):
    """to take parameters and get a correct response"""
    x=input(question+" "+var).lower()
    options = option1+","+option2+ ","+option3
    while x not in  options:
         x=input(question)
    return  x
        

#plains function
def plains():
    print(plainart)#found in ascii file
    print("""\nyou are wandering around in the open plains with grass all
around you see a town in the distance and mountains on the horizon
but you could also stay in the plains and explore""")
    direction=askQuestion("where would you like to go 'Mountains, plains, town'","mountains","town","plains")
    if direction=="mountains":
        print("\nyou decide to move towards the mountains")
        mountains()
    elif direction=="town":
        print("\nyou decide to move towards the Town")
        town()
    elif direction=="plains":
        print("\nyou stay in the plains and over time the endless grass bores you to death")
        game_over()
    
            

#town function
def town():
    print(townart)
    print("""\n The guards to town nod as you walk past asking you not to cause any trouble while you're here
as you look around you see that there are to parts to the town west and east
east looks run down with not much to do while the west has stores and inns """)
    town_choice=askQuestion("west, east","west","east")
    if town_choice=="west":
        print("\nyou move on to west side of town")
        west_town()
    elif town_choice=="east":
        print("\nyou move on to east side of town")
        east_town()


#west_ town function         
def west_town():
    print(west_townart)
    print(""" \nas you walk into the west side of town  you notice all of the buiding are upkept and neat
the store is open and the inn looks inviting there the entire area is inviting
except for one warehouse at the end of the street that place looks scary""")

    west_choice=askQuestion("store, warehouse, inn","store","inn","warehouse")
    if west_choice=="store":
        print("\nyou enter the store")
        store()
    elif west_choice=="inn":
        print("\nyou enter the inn")
        inn()
    elif west_choice=="warehouse":
        print("""\nyou enter the warehouse to find a gang of thieves
they immediately slit your throat before you can even regret your decision to enter the building""")
        game_over()

#store function      
def store():
    print(storeart)
    print("""\nyou walk into the store and
the shopkeeper a little, old woman welcomes you into her shop
you immeadiately see a shiny sword that will help you on your quest
do you want to steal it or buy it""")

    store_choice=askQuestion("steal or buy","steal","buy")
    if store_choice=="steal":
        print("\nthe guards that have been watching you since you arrived tackle you and arrest you for stealing the sword")
        game_over() 
    elif  store_choice=="buy":
        global attack
        if attack==0:
            attack+=2
            print("\nyou buy the sword and decide that you should head back to the plains ")
            plains()
        else:
            print("you alrready bought the sword you just got stabbed through the heart with")
            game_over()

#inn function
def inn():
    print(innart)
    print("""\nyou enter the inn and talk to the inn keeper
he will give you food and room for the night
or you could punch him in the face""")
    inn_choice=askQuestion("punch or sleep","punch","sleep")
    if inn_choice=="punch":
        print("\nyou decide to punch the guy in the face alerting the guards outside and you get arrested ")
        game_over()
    elif inn_choice=="sleep":
        print("""\nYou take the food and bed and sleep soundly during the night, in the morning the innkeeper
offers you a job and you take it, living out the rest of your days in the town""")
        win()
        
    

# east town function
def east_town():
    print(east_townart)
    print("""\n you decide to enter the east side off town and you see a bar nearby
you think that might be a good place to go but out off the corner of your eye
you see a hermit hiding in an alleyway talking to himself""")
    east_choice=askQuestion("hermit, bar","bar","hermit")
    if east_choice=="bar":
        print("\nyou go to the bar")
        bar()
    elif east_choice=="hermit":
        print("\nyou move towards the hermit and talk to him for a bit and he tells you about a secret cave in the"+
              " mountains and that the krakens secret is hidden in another cave and so you return to the plains ")
        global secret
        secret="you then see the hidden cave the hermit told you about, enter hidden to enter"
        plains()
        
#bar function
def bar():
    print(barart)
    print("""\nAs you enter the bar you see several groups of people
so far gone that they can't even remember their own name
as you aproac the barkeep you ead a sign that says no fighting""")
    bar_choice=askQuestion("fight or drink","fight","drink")
    if bar_choice=="fight":
        print("\nyou foolishly decide to stat a fight and punch the barkeep in the face\n as you do you anger the other patrons and they get up and kill you and several others")
        game_over()
    elif bar_choice=="drink":
        print("you start drinking several jugs of ale while you are drunk a thief comes up and steals your money purse\n leaving you unable to pay for the alcohol in retribution the tavernkeep takes your life")
        game_over()
        
#mountain Function
def mountains():
    print(mountainart)
    print("""\nyou look towards the ountains and start the journey towards them
along your way you walk into a crossroads one leading towards the mountains
and another leading to what seems to be the beach""")
    mountain_choice=input("\nmountains or beach")
    if mountain_choice=="mountains":
        print("\nyou continue on to the mountains")
        mountain_path()
    elif mountain_choice=="beach":
        print("\n you move to the beach")
        beach()
#mountain path function
def mountain_path():
    print(peakart)
    global secret
    print("""\n you finally arrive at the mountain and you look to the peak and start climbing
after a while you notice a spring  and wonder if you should stop for a break
and you feel like there should be something more""",secret)
    path_choice=askQuestion("peak or spring","peak","spring","hidden")

    if path_choice=="peak":
        print("you continue your climb to the peak but on your way up you die because you were ill prepared")
        game_over()
    elif path_choice=="spring":
        print("you choose to rest at the spring before you finish your climb and you make it to the peak of the mountain")
        win()
    elif path_choice=="hidden":
        print(hiddenart)
        print("Congratulations you found one of the secret hidden endings \nthe cave is filled with gold bars and enough food to last the rest of your life")
        win()


            
# beach function
def beach():
    print(beachart) 
    print("""\n when you get to the beach you see a ship in the ocean next to you
they are anchored next to a big cave that seems interesting
the warm sand is very alluring and you feel compelled to sleep""")
    beach_choice=askQuestion("boat, cave, sleep","boat","cave","sleep")
    if beach_choice=="boat":
        print("\n you get on the boat")
        boat()
    elif beach_choice=="cave":
        print("you enter the cave")
        cave()
    elif beach_choice=="sleep":
        print("you fall asleep on the beach and are killed by giant crabs that crawl out of the ground")
        game_over()

#boat function
def boat():
    print(boatart)
    global kraken
    print("""\n you choose to help the sailors load up their ship and they
offer to give you a ride to where ever you want to go
but after a while at sea you are attacked by a kraken""")
    kraken_choice=askQuestion("attack,flee","attack","flee","",kraken)
    if kraken_choice=="attack":
        print("you start the attack")
        kraken_attack()
    elif kraken_choice=="flee":
        print("you stupidly decide to try and flee and the kraken destroys your ship")
        game_over()
    elif kraken_choice==kraken:
        print(hiddenart)
        print("you found the second secret ending \n you scare off the kraken by throwing garlic at it whenever one hits it drives the kraken insane until it runs away\n they crew members see you as a hero and you join their crew permenantly")

 # attack sequence           
def kraken_attack():
    print(attackart)
    global attack
    print("you start the assault on the kraken")
    pHealth=30
    kHealth=60
    x=1
    while x==1:
        player_damage=3+attack
        kraken_damage=5
        critical_damage=player_damage*3
        critical_chance=random.randint(1,3)
        if critical_chance==3:
            print("you score a critical hit you deal",critical_damage,"damage")
            kHealth-=critical_damage
            print("the kraken has",kHealth,"left")
        else:
            print("you deal ",player_damage,"damage")
            kHealth-=player_damage
            print("the kraken has",kHealth,"health left")
        if kHealth<=0:
            x=2
            print("you kill the kraken saving the crew you win")
            win()
        else:
            pHealth-=kraken_damage
        print("you have",pHealth,"health left")
        if pHealth<=0:
            x=2
            print("you die and the ship is doomed")
            game_over()
        flee=input("would you like to flee y/n")
        if flee=="y":
            x=2
            print("the ship took heavy damage while you were being attacked and the crew blamed you  and so they hung you")
            game_over()


#cave function
def cave():
    print(caveart)
    print("\n you enter the cave and see three paths stretching in front of you")
    path=askQuestion("left right center","left","right","center")
    if path=="left":
        print("you see two paths before you")
        path2=askQuestion("left or right","left","right")
        if path2=="left":
            print("you died by falling in a hole")
            game_over()
        elif path2=="right":
            cave_end()
    elif path=="center":
        cave_end()
    elif path=="right":
        print("'you see two paths in front of you")
        path3=askQuestion("left or right","left","right")
        if path3=="right":
            print("you died by collapsing rocks")
            game_over()
        elif path3=="left":
            print("you see three more paths in front of you")
            path4=askQuestion("left right center","left","right","center")
            if path4=="left":
                cave_end()
            elif path4=="right":
                print("you get impaled by spikes")
                game_over()
            elif path4=="center":
                print("you get trapped by a cage door and starve to death")
                game_over()

#end cave function
def cave_end():
    print("you make it to the end of the cave learning the krakens secret from a dead skeletons possesions")
    global kraken
    kraken="weakness"
    print("you return to the beach following the path you entered")
    beach()


#game_over function
def game_over():
    global attack
    global secret
    global kraken
    attack=0
    secret=""
    kraken=""
    print("game over")
    print(gameOverart)
    restart=askQuestion("would you like to play again (y,n)","y","n")
    if restart=="y":
        plains()
    elif restart=="n":
        print("goodbye")

#win function
def win():
    global attack
    global secret
    global kraken
    attack=0
    secret=""
    kraken=""
    print(" you won the game")
    print(winart)
    restart=askQuestion("would you like to play again (y,n)","y","n")
    if restart=="y":
        plains()
    elif restart=="n":
        print("goodbye")

# main function   
def main():
    print("welcome to the game")
    print(titleart)
    start=askQuestion("would you like to play (y,n)","y","n")
    if start=="y":
        print("then let's begin")
        plains()
    elif start=="n":
        print("goodbye then")         

main()
