import math
import ast

from helpers.validation import *

def F(X):
    x = X
    return eval(equation)


equation = input("Enter the Equation to be solved: ")
equation = fix_equation(equation)
print(equation)

while input_validation(equation) == False:
    equation = input("Invalid Syntax, Enter The equation again: ")
    equation = fix_equation(equation)


print("Enter the Minimum: ")
l = int(input())
print("Enter the Maximum: ")
r = int(input())+1

validate_min_max(l, r)


# print(equation)
for i in range(l, r):
    Y = F(i)
    print("@ X = " + str(i) + " Y = " + str(Y));

