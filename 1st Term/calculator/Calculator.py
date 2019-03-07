#nathan broadbent,brandon robbins, cody dzierzon, jared mcmahon
#10/3/2018

def add(num1, num2):
    val=num1 + num2
    return val

def subtract(num1, num2):
    val=num1 - num2
    return val

def divide(num1, num2):
    if num2 == 0:
        print("ERROR THERE WAS A 0")
        main()
    else:
        val=num1 / num2
        return val
    

def multiply(num1, num2):
    val= num1* num2
    return val
def modulous(num1,num2):
    if num2 == 0:
        print("ERROR THERE WAS A 0")
        main()
    else:
        val=num1 % num2
        return val

def get_int(message):
    num=input(message)

    if num.isdigit():
        num=int(num)
        return num
    else:
        print("that's not a number")
        get_int(message)

def get_operator(message):
    print(message)
    oper=input("""
+
-
/
*
%""")
    
    return oper
    
    
def check_math(test_value,operator,num1,num2):
    value=test_value
    oper=operator
    num1=num1
    num2=num2

    if oper=="+":
         test=num1+num2
    elif oper=="-":
         test=num1-num2    
    elif oper=="*":
        test=num1*num2   
    elif oper=="/":
         test=num1/num2    
    elif oper=="%":
         test=num1%num2

    if test==value:
        return True
    else:
        return False
def main():
    num1=get_int("enter a first number")
    num2= get_int("enter your second number")

    oper= get_operator("enter an operator")
         
    if oper=="+":
        value=add(num1, num2)
    elif oper=="-":
        value=subtract(num1, num2)
    elif oper=="*":
        value=multiply(num1, num2)
    elif oper=="/":
        value=divide(num1, num2)
    elif oper=="%":
        value=modulous(num1, num2)

    true_value=check_math(value, oper, num1, num2)
    if true_value:
        print(value)
    else:
        print("the double check failed")
        
main()
