import time


class Critter(object):

    def __init__(self, name):
        self.name = name
        self.__hunger = 0
        self.__boredom = 0
        self.__birth = time.localtime()
        self.last_time = time.localtime()

    @property
    def mood(self):
        unhappiness = self.__boredom+self.__hunger
        if unhappiness < 5:
            mood = "happy"
        elif 6 <= unhappiness <= 10:
            mood = "okay"
        elif 11 <= unhappiness <= 15:
            mood = "frustrated"
        else:
            mood = "mad"

        return mood

    def __pass_time(self, amount, food, play):
        mins = self.get_time()
        if food == 0:
            self.__hunger += 1 + (amount//4) + (mins//10)
        if play == 0:
            self.__boredom += 1 + (amount//4) + (mins//10)

    def play(self, play=4):
        print("you have played with your critter and lowered it's boredom ")
        self.__boredom -= play
        if self.__boredom < 0:
            self.__boredom = 0
        self.__pass_time(play,0,1)

    def talk(self):
        print("my name is", self.name,"I am feeling", self.mood,
              "\nbecause my hunger is", self.__hunger, "\nand my boredom is is ", self.__boredom)
        years, months, days, hours, mins = self.get_age()
        print("I am", years, "years,", months, "months", days, "days old", hours, "hours and", mins, "minutes old\n")
        self.__pass_time(0,0,0)

    def eat(self, food=4):
        print("you have fed your critter and lowered it's hunger ")
        self.__hunger -= food
        if self.__hunger < 0:
            self.__hunger = 0
        self.__pass_time(food,1,0)

    def get_time(self):
        new_time = time.localtime()
        years_past = new_time[0] - self.last_time[0]
        months_past = new_time[1] - self.last_time[1]
        days_past = new_time[2] - self.last_time[2]
        hour_past = new_time[3] - self.last_time[3]
        mins_past = new_time[4] - self.last_time[4]
        months = months_past+(years_past*12)
        days = days_past + ((months // 12) * 365)
        hours = hour_past + (days * 24)
        mins = mins_past + (hours * 60)
        self.last_time = new_time
        return mins

    def get_age(self):
        new_time = time.localtime()
        years_past = new_time[0] - self.__birth[0]
        months_past = new_time[1] - self.__birth[1]
        days_past = new_time[2] - self.__birth[2]
        hour_past = new_time[3] - self.__birth[3]
        mins_past = new_time[4] - self.__birth[4]
        return years_past, months_past, days_past, hour_past, mins_past


def main():
    name = input("what is your critters name")
    critter = Critter(name)
    choice = None
    while choice != "0":
        print("would you like to\ntalk to your critter 1\nfeed your critter 2\nplay with your critter 3\nor exit 0")
        choice = input()
        if choice == '0':
            print("good bye")
            break
        elif choice == '1':
            critter.talk()
        elif choice == '2':
            amount = int(input("how many pounds of food would you like to give to the critter"))
            critter.eat(amount)
        elif choice == '3':
            amount = int(input("how long would you like to play with the critter"))
            critter.play(amount)
        else:
            print("not a good choice")


main()
