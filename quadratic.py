# Replace the "ANSWER HERE" for your answer
import math

def roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        r1 = (-b + math.sqrt(discriminant)) / (2 * a)
        r2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"({r1}, {r2})"
    elif discriminant == 0:
        r = -b / (2 * a)
        return f"({r})"
    else:
        return "( )"

#roots()


def value_y(a, b, c, x):
    return a * x ** 2 + b * x + c

#value_y()


def to_string(a, b, c):
    if a != 0 and b != 0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a != 0 and b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    elif a == 0 and b != 0:
        return f"f(x) = {b} * X + {c}"
    else:
        return f"f(x) = {c}"
    
#to_string()


def derivation(a, b, c):
    da = 2 * a
    db = b
    if da != 0 and db != 0:
        return f"f'(x) = {da} * X + {db}"
    elif da != 0 and db == 0:
        return f"f'(x) = {da} * X"
    elif da == 0 and db != 0:
        return f"f'(x) = {db}"
    else:
        return "f'(x) = 0"
    
#derivation()
