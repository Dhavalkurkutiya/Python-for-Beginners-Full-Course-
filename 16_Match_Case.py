# 1. What is match case statment ?
# Ans: The match case statement is used to execute one block of code from multiple conditions.

# 2. What is the difference between if else and match case statement ?
# Ans: The if…else statement is used to execute two different blocks of code depending on whether the specified condition is true. The match case statement is used to execute one block of code from multiple conditions.

x = int(input("Enter the number: "))
match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")
    case 4:
        print("x is 4")
    case 5:
        print("x is 5")
    case _:
        print("x is not 1, 2, 3, 4, 5")