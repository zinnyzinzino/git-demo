import math
def solution(a,b,c):
    #discriminant
    d = b**2 - 4*a*c
    if d < 0:  
        print("No real roots")
        return []
    elif d == 0:
        x = -b / (2*a)
        return [x]
    else:
        sqrt_d = math.sqrt(d)
        x1 = (-b + sqrt_d) / (2*a)
        x2 = (-b - sqrt_d) / (2*a)
        roots = tuple(sorted([x1, x2]))
        return roots
    
    
print(solution(1, -3, 2))
print(solution(1, 4, 4))
print(solution(1, 3, 45))