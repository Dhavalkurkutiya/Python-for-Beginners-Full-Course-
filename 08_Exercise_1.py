
print("Enter the first number")
a = int(input())
print("Enter the second number")
b = int(input())
print("Enter the operator")
op = input()

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid operator")
    