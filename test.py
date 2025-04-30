from sys import stdin
input=lambda:stdin.readline().rstrip()

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def verticality(x1, y1, x2, y2, x3, y3):
    uierator = abs((y2-y1)*x3 - (x2-x1)*y3 + x2*y1 - y2*x1)
    denominator = ((y2-y1)**2 + (x2-x1)**2)**0.5
    return uierator / denominator

def horizontal(x1, y1, x2, y2, x3, y3):
    t = ((x3-x1)*(x2-x1) + (y3-y1)*(y2-y1)) / ((x2-x1)**2 + (y2-y1)**2)
    return (x1 + t*(x2-x1), y1 + t*(y2-y1))


def monotoneChain():
    upper, lower = [], []
    
    for point in points:
        while len(lower)>1 and ccw(*lower[-2], *lower[-1], *point) <= 0:lower.pop()
        lower.append(point)
    lower.pop()
    
    for point in points[::-1]:
        while len(upper)>1 and ccw(*upper[-2], *upper[-1], *point) <= 0:upper.pop()
        upper.append(point)
    upper.pop()
    
    return lower+upper, len(lower)

def transverse(stack, a, b, c):
    size = len(stack)
    p = horizontal(*stack[a], *stack[b], *stack[c])

    left, lt = 0, 0
    flag = a+1
    while flag!=c:
        flag = (flag-1)%size
        if ccw(*stack[c], *p, *stack[flag])>0:continue
        
        new = verticality(*stack[c], *p, *stack[flag])
        if new>left:left, lt = new, flag
        else:break

    right, rt = 0, 0
    flag = b-1
    while flag!=c:
        flag = (flag+1)%size
        if ccw(*stack[c], *p, *stack[flag])<0:continue

        new = verticality(*stack[c], *p, *stack[flag])
        if new>right:right, rt = new, flag
        else:break
    return left+right, lt, rt

def setting(stack, li, ui):
    size = len(stack)
    
    while True:
        a, b = stack[li], stack[(li+1)%size]
        c, d = stack[ui], stack[(ui+1)%size]
        
        point1 = b[0]-a[0], b[1]-a[1]
        point2 = d[0]-c[0], d[1]-c[1]

        if ccw(*point1, 0, 0, *point2)>0:
            row, lt, rt = transverse(stack, li, (li+1)%size, ui)
            col = verticality(*stack[li], *stack[(li+1)%size], *stack[ui])
            
            return row+col, lt, li, rt, ui
        else:ui = (ui+1)%size

n = int(input())
points = [list(map(int, input().split()))for _ in range(n)]
points.sort()

if n==2:print(distance(*points[0], *points[1])*2)
else:
    stack, cnt = monotoneChain()
    print(stack)
    print(setting(stack, 0, cnt))