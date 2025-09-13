"""
Module containing three simple maths functions:
summation, subtraction, and multiplication
"""

def summation(a, b):
    """
    Takes numbers a and b as inputs and returns their sum.
    Both a and b can be either an integer or float
    """
    if (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        # Return answer if both a and b are ints or floats
        return a + b

    # Return None if a and/or b is not an int or float
    return None

def subtraction(a, b):
    """
    Takes numbers a and b as inputs and returns a minus b.
    Both a and b can be either an integer or float
    """
    if (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        # Return answer if both a and b are ints or floats
        return a - b

    # Return None if a and/or b is not an int or float
    return None

def multiplication(a, b):
    """
    Takes numbers a and b as inputs and returns their product.
    Both a and b can be either an integer or float
    """
    if (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        # Return answer if both a and b are ints or floats
        return a * b

    # Return None if a and/or b is not an int or float
    return None
