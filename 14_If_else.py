# 1. What is if else statement ?
#  Ans: The if…else statement is used to execute two different blocks of code depending on whether the specified condition is true.


apple = int(input("Enter the number of apples: "))
banana = int(input("Enter the number of bananas: "))

if apple > banana:
    print("Apple is greater than Banana")

elif apple == banana:
    print("Apple is equal to Banana")

elif apple < banana:
    print("Apple is less than Banana")

else:
    print("Banana is greater than Apple")
