import math

def solution(a, b, c):
    d = b**2 - 4 * a * c
    
    if d < 0:
        return ()
    
    elif d == 0:
        x = -b / (2 * a)
        return (float(x),)
        
    else:
        sqrt_d = math.sqrt(d)
        x1 = (-b - sqrt_d) / (2 * a)
        x2 = (-b + sqrt_d) / (2 * a)
        
        return tuple(sorted((float(x1), float(x2))))