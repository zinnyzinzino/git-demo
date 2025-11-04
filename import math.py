import math
def calculate_experssion(a,b):
  result = (12*a + 25*b) / (1 + a**(2**b))
  return round(result, 2)


print(calculate_experssion(2,3))
