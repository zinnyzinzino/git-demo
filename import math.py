import math
def some_expression_with_rounding(a, b):
    result = (12 * a + 25 * b) / (1 + a ** (2 ** b))
    return round(result, 2)

print(some_expression_with_rounding(123, 1))
print(some_expression_with_rounding(1.4, 2.55))