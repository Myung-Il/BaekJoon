def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3
a = 2, -3
b = 2, 300
c = 104, 297
print(ccw(*a, *b, *c))