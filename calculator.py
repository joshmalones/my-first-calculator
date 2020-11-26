from os import add_dll_directory


print("Welcome to my first program")

def game(num1,num2,operator):



 
    if operator == "+":
        add = num1 + num2
        answer = str(add)
        print(num1, " + ", num2, " = ", answer)
    elif operator == "-":
        subtrack = num1 - num2
        answer = str(subtrack)
        print(num1, " - ", num2, " = ", answer)
    elif operator == "*":
        multiply = num1 * num2
        answer = str(multiply)
        print(num1, " * ", num2, " = ", answer)
    elif operator == "/":
        divide = num1 / num2
        answer = str(divide)
        print(num1, " / ", num2, " = ", answer)
    else:
       print("invalid")


yOrNo = input("do you want to play? ( Yes / No ) : ").lower();

if yOrNo == "yes":
    num1 = int(input("What is your first number? : "))
    operator = input("What is your operator? : ")
    num2 = int(input("What is your second number? : "))
    game(num1,num2,operator)

elif yOrNo == "no":
    print("Are you sure you don't want to play?")

else:
    print("invalid answer")
    pass
