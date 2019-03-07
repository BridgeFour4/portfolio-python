# Nathan Broadbent
#3/4/2019

#imports
import random
import time
#classes
class Person(object):
    def __init__(self,name):
        self.name=name
        self.role=[]

    def display_roles(self):
        print(self.name)
        for i in self.role:
            if i:
                print(i)
        print("")

    def clear_roles(self):
        self.role=[]


#methods
def ask_num(message, min, max):
    """ask for a number within a range
    when you call this up you will pass in a string message a minimum value
    and a maximum value
    ask_num("enter a number between 2-7",2,7)"""
    while True:
        try:
            number = int(input(message))
        except:
            print("that was not a number")
            continue
        if max >= number >= min:
            break
    return number


def ask_yes_no(question):
    """this is to be used for asking yes or no questions
    when you call it up you need a catching variable for the
    yes or no value as a y or n
    ask_yes_no("is 2+2 = 4")
    """
    response = None
    while response not in ("y", "n"):
        response = input(question+" y or n").lower()
    return response


def assign_roles(weeks,people,roles):
    week=1
    for i in range(weeks):
        random.shuffle(roles)
        x=0
        if len(people)>len(roles):
            for i in range(len(people)):
                people[i].role.append(roles[x])
                x+=1
                if x ==len(roles):
                    x=0
        elif len(roles)>len(people):
            for i in range(len(roles)):
                people[x].role.append(roles[i])
                x+=1
                if x ==len(people):
                    x=0
        else:
            for i in people:
                i.role.append(roles[x])
                x += 1

        print("\nWeek",week,"\n")
        week+=1
        for i in people:
            i.display_roles()
            i.clear_roles()
        time.sleep(2)

# Main Function


def main():

    numpeople=ask_num("how many people need roles",1,8)
    rolenum=ask_num("how many roles are there",1,8)
    people=[]
    roles=[]
    for i in range(numpeople):
        name= input("persons name")
        person=Person(name)
        people.append(person)
    for i in range(rolenum):
        role= input("what is the name of the role")
        roles.append(role)
    while True:
        weeks=ask_num("how many weeks would you like displayed",1,4)
        assign_roles(weeks,people,roles)
        cont = ask_yes_no("would you like to do more weeks")
        if cont == "n":
            break

main()