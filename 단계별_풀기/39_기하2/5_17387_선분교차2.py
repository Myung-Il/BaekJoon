from sys import stdin
input=lambda:stdin.readline().rstrip()


def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3


a1, b1, a2, b2 = map(int,input().split())
a3, b3, a4, b4 = map(int,input().split())

mx1, my1, mx2, my2 = min(a1, a2), min(b1, b2), max(a1, a2), max(b1, b2)
mx3, my3, mx4, my4 = min(a3, a4), min(b3, b4), max(a3, a4), max(b3, b4)

a = ccw(a1, b1, a2, b2, a3, b3)
b = ccw(a1, b1, a2, b2, a4, b4)
c = ccw(a3, b3, a4, b4, a1, b1)
d = ccw(a3, b3, a4, b4, a2, b2)

if a*b==0 and c*d==0:
    if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
        print(1);exit()
elif a*b<=0 and c*d<=0:print(1);exit()
else:                  print(0)