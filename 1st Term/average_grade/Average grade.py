#nathan broadbent
#10/5/18

def average_test(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10):
    test1=int(a1)
    test2=int(a2)
    test3=int(a3)
    test4=int(a4)
    test5=int(a5)
    test6=int(a6)
    test7=int(a7)
    test8=int(a8)
    test9=int(a9)
    test10=int(a10)


    average= test1+test2+test3+test4+test5+test6+test7+test8+test9+test10
    average= average/10
    return average


def average_grade(average):
    average=average

    if  average>=90:
        grade="your grade is an A"
    elif average>=80:
        grade="your grade is an B"
    elif average>=70:
        grade="your grade is an C"
    elif average>=60:
        grade="your grade is an D"
    elif average>=50:
        grade="your grade is an F"
    else:
        grade="something went wrong with the calulations"
    return grade
    
def main():
    a1=input("enter your 1st test score")
    a2=input("enter your 2nd test score")
    a3=input("enter your 3rd test score")
    a4=input("enter your 4th test score")
    a5=input("enter your 5th test score")
    a6=input("enter your 6th test score")
    a7=input("enter your 7th test score")
    a8=input("enter your 8th test score")
    a9=input("enter your 9th test score")
    a10=input("enter your 10th test score")
    final=average_test(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10)

    answer=average_grade(final)
    print("your average is",final,"and",answer)

main()
    
