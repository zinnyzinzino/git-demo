import math
def some_expression_with_rounding(a, b):
    result = (12 * a + 25 * b) / (1 + a ** (2 ** b))
    return round(result, 2)

