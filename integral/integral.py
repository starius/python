def intergral(left, right, precision=0.001, delta_x=0.001):
    def decorator(f):
        points = set([left])
        length = right - left
        shift = length / 2.0
        value = f(left)
        
        while True:
            points |= set([x + shift for x in points])
            
            new_value = 0.0
            for point in points:
                new_value += f(point)
            new_value *= length
            new_value /= len(points)
            
            print shift
            if abs(new_value - value) < precision or shift < delta_x:
                return new_value
            value = new_value
            shift /= 2.0
    return decorator
    
    
import math


@intergral(0, 3.14, 10**-20)
def two(x):
    return math.sin(x)
   

print two
