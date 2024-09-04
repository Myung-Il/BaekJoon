from sys import stdin
input=lambda:stdin.readline().rstrip()

from sys import stdin
input=lambda:stdin.readline().rstrip()


def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3


a1, b1, a2, b2 = map(int,input().split())
a3, b3, a4, b4 = map(int,input().split())

a = ccw(a1, b1, a2, b2, a3, b3)
b = ccw(a1, b1, a2, b2, a4, b4)
c = ccw(a3, b3, a4, b4, a1, b1)
d = ccw(a3, b3, a4, b4, a2, b2)
print(1 if a*b<=0 and c*d<=0 and (a1<=a3<=a2 or a1<=a4<=a2) else 0)