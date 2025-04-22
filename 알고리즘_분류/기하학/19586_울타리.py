from sys import stdin
input=lambda:stdin.readline().rstrip()

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def height(x1, y1, x2, y2, x3, y3):
    px1, py1 = x1-x2, y1-y2
    px2, py2 = x3-x2, y3-y2

    cross = abs(px1*py2 - py1*px2)
    base_len = (px2**2 + py2**2) ** 0.5
    return cross / base_len


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
    
    return lower, upper

def rotatingCalipers(lower, upper):
    stack = lower+upper
    size = len(stack)
    
    li, ui = 0, len(lower)
    l = [0]*size

    cnt = 0
    while cnt!=size:
        a, b = stack[li], stack[(li+1)%size]
        c, d = stack[ui], stack[(ui+1)%size]
        
        point1 = b[0]-a[0], b[1]-a[1]
        point2 = d[0]-c[0], d[1]-c[1]

        if ccw(*point1, 0, 0, *point2)>0:
            li = (li+1)%size
            cnt += 1
        else: ui = (ui+1)%size
        l[li] = [li, ui]
    return l

def solve(stack, under):
    result = 0
    size = len(stack)

    for u, t in under:...



n = int(input())
points = [tuple(map(int,input().split()))for _ in range(n)]
points.sort()

con1, con2 = monotoneChain()
rot = rotatingCalipers(con1, con2)
stack = con1+con2

print(solve(stack, rot))