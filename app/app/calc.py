

def add(x, y):
    """ Add two numbers together"""
    if type(x) and type(y) not in [int, float]:
        raise TypeError("The entered value is not an integer or a float")
    return x + y

def substract(a, b):
    """ Substract one number from another"""
    return b - a
