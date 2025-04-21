from sys import stdin
from math import pi
input=lambda:stdin.readline().rstrip()

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5


def monotoneChain():
    upper, lower = [], []
    
    for point in points:
        while len(lower)>1 and ccw(*lower[-2], *lower[-1], *point) <= 0:lower.pop()
        lower.append(point)
    lower.pop()
    
    for point in reversed(points):
        while len(upper)>1 and ccw(*upper[-2], *upper[-1], *point) <= 0:upper.pop()
        upper.append(point)
    upper.pop()

    return lower+upper

def solve():
    size = len(stack)
    arc = (pi/2) * l


n, l = map(int, input().split())
points = [list(map(int, input().split()))for _ in range(n)]
points.sort()
stack = monotoneChain()

size = len(stack)
result = 2*pi*l
for idx in range(1, size+1):
    p1 = stack[(idx-1)%size]
    p2 = stack[idx%size]
    result += distance(*p1, *p2)

print(round(result))