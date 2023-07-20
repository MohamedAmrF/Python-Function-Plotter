import math
import ast
import matplotlib.pyplot as plt
import numpy as np
from helpers.validation import *

def F(X):
    """Takes X and returns F(x)

    Args:
        X (float): input value to the equation (x)

    Returns:
        float: Output of the function after evaluation (F(x))
    """
    x = X
    return eval(equation)


equation = input("Enter the Equation to be solved: ")
equation = fix_equation(equation)
validate(equation)


print("Enter the Minimum: ")
l = int(input())
print("Enter the Maximum: ")
r = int(input())+1

validate_min_max(l, r)


xpoints = np.arange(l,r)
ypoints = np.zeros(r-l)

print(int(xpoints.size))
print(int(ypoints.size))

for i in range(l, r):
    ypoints[i-l] = F(i)

plt.plot(xpoints, ypoints)
plt.show()

# plot
# for i in range(l, r):
#     Y = F(i)
#     print("@ X = " + str(i) + " Y = " + str(Y));

