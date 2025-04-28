from sys import stdin
input=lambda:stdin.readline().rstrip()

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def verticality(x1, y1, x2, y2, x3, y3):
    numerator = abs((y2-y1)*x3 - (x2-x1)*y3 + x2*y1 - y2*x1)
    denominator = ((y2-y1)**2 + (x2-x1)**2)**0.5
    return numerator / denominator

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

def rotatingCalipers(stack, num):
    size = len(stack)
    
    li, ui = 0, num
    squarepoints = [[0, 0, 0]for _ in range(size)]
    squarepoints[li][1] = stack[ui]
    
    cnt = 0
    while cnt!=size:
        a, b = stack[li], stack[(li+1)%size]
        c, d = stack[ui], stack[(ui+1)%size]
        
        point1 = b[0]-a[0], b[1]-a[1]
        point2 = d[0]-c[0], d[1]-c[1]

        if ccw(*point1, 0, 0, *point2)>0:
            li = (li+1)%size
            cnt+=1
            squarepoints[li][1] = c
        else:
            ui = (ui+1)%size
            squarepoints[li][1] = d
            
    for li in range(size):
        a, b = stack[li], stack[(li+1)%size]
        squarepoints[li][2] = distance(*a, *b)
        
        ui = (li+2)%size
        while (c:=stack[ui])!=squarepoints[li][1]:
            ui = (ui+1)%size
            p = horizontal(*a, *b, *c)
            squarepoints[li][2] = max(squarepoints[li][2], distance(*a, *p))
        
        ui = (li-1)%size
        while (c:=stack[ui])!=squarepoints[li][1]:
            ui = (ui-1)%size
            p = horizontal(*a, *b, *c)
            squarepoints[li][0] = max(squarepoints[li][0], distance(*a, *p))
        
        squarepoints[li][1] = verticality(*a, *b, *squarepoints[li][1])
            
    return squarepoints

def solve(square):
    mx = 0
    for left, col, right in square:
        row = left+right
        mx = max(mx, (row+col)*2)


n = int(input())
points = [list(map(int, input().split()))for _ in range(n)]
points.sort()

stack, cnt = monotoneChain()
square = rotatingCalipers(stack, cnt)
print(square)
print(solve(square))