def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3

'''
1 1 3 3
2 3 1 4

'''
print(ccw(1, 1, 3, 3, 1, 3))