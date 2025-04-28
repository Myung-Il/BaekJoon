import math

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3

a = 0, 0
b = 0, 1
c = 1, 1
print(ccw(*a, *b, *c))