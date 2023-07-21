import math
import ast

def validate_min_max(l, r):
    if r <= l:
        return False
    return True

def validate(input_equation):
    while input_validation(input_equation) == False:
        input_equation = input("Invalid Syntax, Enter The equation again: ")
        input_equation = fix_equation(input_equation)

def valid_character(c):
    validCharacters = "x+-*/^ 0123456789()"
    if validCharacters.find(c) == -1:
        return False
    else:
        return True

def input_validation(input_equation):
    # Check for python syntax errors
    try:
        ast.parse(input_equation)
    except SyntaxError:
        return False

    # Check for valid input characters
    for c in input_equation:
        if not valid_character(c):
            return False
    return True

def fix_equation(input_equation):
    input_equation = input_equation.replace("^", "**")
    input_equation = input_equation.replace("X", "x")
    return input_equation

def F(X, equation):
    """Takes X and returns F(x)

    Args:
        X (float): input value to the equation (x)

    Returns:
        float: Output of the function after evaluation (F(x))
    """
    x = X
    return eval(equation)