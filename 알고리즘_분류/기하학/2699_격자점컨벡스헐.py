from sys import stdin
from math import ceil
input = lambda:stdin.readline().rstrip()

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3


def monotoneChain():
    right, left = [], []
    
    for point in points:
        while len(left)>1 and ccw(*left[-2], *left[-1], *point) >= 0:left.pop()
        left.append(point)
    left.pop()
    
    for point in reversed(points):
        while len(right)>1 and ccw(*right[-2], *right[-1], *point) >= 0:right.pop()
        right.append(point)
    right.pop()

    return left+right


for _ in range(int(input())):
    n = int(input())
    points = []

    for _ in range(ceil(n/5)):
        sub = list(map(int, input().split()))
        for idx in range(0, len(sub)-1, 2):
            points.append((sub[idx], sub[idx+1]))
    points.sort(key=lambda p:(-p[1], p[0]))

    stack = monotoneChain()
    print(len(stack))
    for x, y in stack:
        print(x, y)