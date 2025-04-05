from sys import stdin
from math import acos, sin, pi
input=lambda:stdin.readline().rstrip()


def theta(r1, r2, d):
    return acos((r1**2+d**2-r2**2)/(2*r1*d))*2

def area(r, th):
    return r**2*sin(th)/2

def lr(r, x):
    return x*r**2


x1, y1, r1, x2, y2, r2 = map(float,input().split())

d = ((x1-x2)**2+(y1-y2)**2)**0.5
def solve():
    if r1+r2<=d:return 0
    elif abs(r1-r2)>=d:return min(r1, r2)**2*pi
    else:
        th1 = theta(r1, r2, d)
        th2 = theta(r2, r1, d)

        A1 = lr(r1, th1)/2 - area(r1, th1)
        A2 = lr(r2, th2)/2 - area(r2, th2)
        return A1 + A2
print(f"{solve():.3f}")