#nathan broadbent, kaleb beck,zach page
#11/18
import random
#questions
upperQ="this function turns all letters in a string into capital letters: what is the term"
titleQ="this function capitalizes the first letter of every word: what is the term"
flowChartQ="used to show how a program flows: what is the term"
intQ="a whole number data type: what is the term"
stringQ="a list of characters surrounded by quotations: what is the term"
indexQ="a specific position in a string what is the term: what is the term"
functionQ=" a block of code that you can call whenever: what is the term"
variableQ="a defined value that can be called: what is the term"
commentQ="a line of code that the computer doesn't read: what is the term"
loopQ="a block of code that repeats itself: what is the term"
upper="upper"
title="title"
flowchart="flowchart"
integer="int"
string="string"
index="index"
function="function"
variable="variable"
comment="comment"
loop="loop"
#ists
triviaList=[upperQ,titleQ,flowChartQ,intQ,stringQ,indexQ,functionQ,variableQ,commentQ,loopQ]
wordList=[upper,title,flowchart,integer,string,index,function,variable,comment,loop]
#defining the puzzle
puzzle1="fqvindexkoclyaxepnffugohriludgvlbwninttxgkrtccaniognretheblttziipmaolpewormporsesnbotpugtzlscwsswjfe"
#score variable
score=0
#finds a random question and returns it
def randomQuestion():
    print("enter quit at anytime to skip the question")
    x=0
    while x<=9:
        randNum=random.randrange(len(triviaList))
        question=triviaList[randNum]
        answer=wordList[randNum]
        del triviaList[randNum]
        del wordList[randNum]
        askQuestion(question,answer,puzzle1)
        print("your score is now",score)
        x+=1      
# the trivia part of the game
def askQuestion(tQuestion,word,puzzle):
    attempts=10
    global score
    #fullQuestion=tQuestion,"what is the term"
    while True:
        answer=input(tQuestion)
        if answer.lower()=="quit":
            break
        if answer.lower()==word:
            print("correct")
            score+=attempts*5
            puzzleSolve(word,attempts,puzzle)
            break
        else:
            attempts-=1
            print(attempts,"attempts left")
# the puzzle part of the game        
def puzzleSolve(word,attempts,puzzle):
    global score
    display="where is "+word+" at in the puzzle put a comma between the index's and at the end"
    while True:
        displaypuzzle(puzzle)
        answer=input(display)
        if answer.lower()=="quit":
            break
        input_number=""
        new_word=""
        for i in answer:         
            if i ==",":
                if input_number.isdigit():
                    input_number=int(input_number)
                    new_word+=puzzle[input_number]
                    input_number=""
                else:
                    break
            else:    
                input_number+=i  
        if new_word==word:
            print("correct")
            score+=attempts*10
            break
        else:
            attempts-=1
            print(attempts,"attempts left")
#displaying  the puzzle
def displaypuzzle(puzzle):
    print("  0123456789")
    print("0",puzzle[0:10])
    print("1",puzzle[10:20])
    print("2",puzzle[20:30])
    print("3",puzzle[30:40])
    print("4",puzzle[40:50])
    print("5",puzzle[50:60])
    print("6",puzzle[60:70])
    print("7",puzzle[70:80])
    print("8",puzzle[80:90])
    print("9",puzzle[90:])
    print()
#main menu
def main():
    print("you get 10 attempts per question  after that your score will go into the negatives")
    randomQuestion()
    print("your final score is",score)
    continuey=input("would you like to play again y/n ")
    if continuey.lower()=="y":
        main()
    
main()
