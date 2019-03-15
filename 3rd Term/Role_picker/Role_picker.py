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
        self.bias="";

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
    roles2nd=[]
    for i in range(weeks):
        z=0
        if len(people)>len(roles):
            roles2nd = []
            for i in roles:
                roles2nd.append(i)
            for i in range(len(people)):
                print(roles2nd)
                if len(roles)==1:
                    people[i].role.append(roles[0])
                    continue
                else:
                    try:
                        roles2nd.remove(people[i].bias)
                        p=1
                    except:
                        print()
                        p=0
                    if len(roles2nd)==0:
                        roles2nd.append(people[i].bias)
                    x=random.choice(roles2nd)
                    people[i].role.append(x)
                    roles2nd.remove(x)
                    if people[i].bias !="" and p==1:
                        roles2nd.append(people[i].bias)
                    if len(roles2nd)==0:
                        for role in roles:
                            roles2nd.append(role)
                    people[i].bias = x

        elif len(roles)>len(people):
            roles2nd = []
            for i in roles:
                roles2nd.append(i)
            for i in range(len(roles)):
                print(roles2nd)
                try:
                    roles2nd.remove(people[z].bias)
                    p = 1
                except:
                    print()
                    p = 0
                if len(roles2nd) == 0:
                    roles2nd.append(people[z].bias)
                x = random.choice(roles2nd)
                people[z].role.append(x)
                roles2nd.remove(x)
                if people[z].bias != "" and p == 1:
                    roles2nd.append(people[z].bias)
                people[z].bias = x
                z+=1
                if z ==len(people):
                    z=0
        else:
            roles2nd=[]
            for i in roles:
                roles2nd.append(i)
            for person in people:
                if len(people)==1:
                    person.role.append(Roles2nd[0])
                    continue
                else:
                    print(roles2nd)
                    try:
                        roles2nd.remove(person.bias)
                        p=1
                    except:
                        print()
                        p=0
                    if len(roles2nd)==0:
                        roles2nd.append(person.bias)
                    x=random.choice(roles2nd)
                    person.role.append(x)
                    roles2nd.remove(x)
                    if person.bias !="" and p==1:
                        roles2nd.append(person.bias)
                    person.bias = x




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