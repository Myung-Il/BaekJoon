from sys import stdin
input = lambda:stdin.readline().rstrip()

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3


def monotoneChain():
    upper, lower = [], []
    
    for point in points:
        while len(lower)>1 and ccw(*lower[-2], *lower[-1], *point) < 0:lower.pop()
        lower.append(point)
    lower.pop()
    
    for point in reversed(points):
        while len(upper)>1 and ccw(*upper[-2], *upper[-1], *point) < 0:upper.pop()
        upper.append(point)
    upper.pop()

    return lower+upper


n = int(input())
points = []
for _ in range(n):
    x, y, c = input().split()
    if c=="Y":points.append(list(map(int, (x, y))))
points.sort()

stack = monotoneChain()

print(len(stack))
for point in stack:
    print(*point)