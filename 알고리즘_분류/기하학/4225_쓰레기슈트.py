from sys import stdin
import math
input=lambda:stdin.readline().rstrip()

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def height(x1, y1, x2, y2, px, py):
    ax, ay = px - x1, py - y1
    bx, by = x2 - x1, y2 - y1

    cross = abs(ax*by - ay*bx)
    base = ((bx)**2 + (by)**2)**0.5
    return cross/base

def ceil2(x):
    exm = x*100
    if exm%1:return math.ceil(exm)/100
    else: return exm/100


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


turn = 0
while True:
    turn += 1

    n = int(input())
    if not n:break
    points = [list(map(int, input().split()))for _ in range(n)]
    points = sorted(points)

    stack = monotoneChain()
    size = len(stack)
    result = float("inf")
    for idx1 in range(1, size+1):
        p1 = stack[(idx1-1)%size]
        p2 = stack[idx1%size]

        length = 0
        for idx2 in range(idx1+1, idx1+size-1):
            p3 = stack[idx2%size]

            length = max(length, height(*p1, *p2, *p3))
        if length:result = min(result, length)
    
    print(f"Case {turn}: {ceil2(result):0.2f}")