import math
equation = input("Enter the Equation to be solved: ")
equation = equation.replace("^", "**")


def F(X):
    x = X
    return eval(equation)


print("Enter the Minimum: ")
l = int(input())
print("Enter the Maximum: ")
r = int(input())

for i in range(l, r+1):
    Y = F(i)
    print("@ X = " + str(i) + " Y = " + str(Y));




