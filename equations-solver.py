def solve(left, right, delta=0.001):
    def decorator(f):
        l, m, r = left, (left + right) / 2.0, right
        while abs(f(m)) > delta:
            m = (l + r) / 2.0
            a, b, c = f(l), f(m), f(r)
            if a == 0:
                return l
            elif b == 0:
                return m
            elif c == 0:
                return r
            elif a * b < 0:
                r = m
            elif b * c < 0:
                l = m
            else:
                raise Exception("Function may not have solution within [%s,%s]" % (l, r))
        return m
    return decorator
    
    
import math


@solve(3, 4)
def pi(x):
    return math.sin(x)
   
   
   
@solve(1, 100000)
def Tboil(T):
    return -3308 / float(T) - 0.8 * math.log10(T) + 10.373 - math.log10(760)
   

print Tboil
