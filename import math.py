import math
def calculate(a,b):
    result = (12 * a + 25 * b) / (1 + a**(2**b))
    return round(result, 2)



print(calculate(123,1))
print(calculate(1.4, 2.55))