from sys import stdin
input=lambda:stdin.readline().rstrip()
INF = float("inf")

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def area(x1, y1, x2, y2, x3, y3):
    return abs(x1*(y2-y3) +x2*(y3-y1) +x3*(y1-y2))/2

def height(x1, y1, x2, y2, px, py):
    underline = distance(x1, y1, x2, y2)
    if not underline:return 0
    
    square = area(x1, y1, x2, y2, px, py)*2
    return square/underline


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
    mxnum = distance(*stack[li], *stack[ui])
    mxpoint = li, ui
    for _ in range(size):
        a, b = stack[li], stack[(li+1)%size]
        c, d = stack[ui], stack[(ui+1)%size]
        
        point1 = b[0]-a[0], b[1]-a[1]
        point2 = d[0]-c[0], d[1]-c[1]

        if ccw(*point1, 0, 0, *point2)>0: li = (li+1)%size
        else: ui = (ui+1)%size
        
        dis = distance(*stack[li], *stack[ui])
        if mxnum<dis:
            mxnum = dis
            mxpoint = li, ui
    return mxpoint

def otherPoint(stack, flag):
    size = len(stack)
    lp, rp = flag[0], flag[1]
      
    il, iu = 0, 0
    mx = -1
    for idxlower in range(lp+1, rp):
        point = stack[idxlower]
        dis = height(*stack[lp], *stack[rp], *point)
        if mx<dis: il, mx = idxlower, dis
        
    mx = -1
    for idxupper in range(rp+1, size):
        point = stack[idxupper]
        dis = height(*stack[lp], *stack[rp], *point)
        if mx<dis: iu, mx = idxupper, dis
        
    return stack[lp], stack[il], stack[rp], stack[iu]

def solve(point):
    square = []
    for idx in range(4):
        dis = distance(*point[idx%4], *point[(idx+1)%4])
        
        case1 = height(*point[idx%4], *point[(idx+1)%4], *point[(idx+2)%4])
        case2 = height(*point[idx%4], *point[(idx+1)%4], *point[(idx+3)%4])
        
        square.append((dis, max(case1, case2)))
    square.sort()

    print(point)
    print(square)
    res = square[3]
    return res[0]*2 + res[1]*2
    

n = int(input())
points = [tuple(map(int,input().split()))for _ in range(n)]
points.sort()

con1, con2 = monotoneChain()
rot = rotatingCalipers(con1, con2)
point = otherPoint(con1+con2, rot)
print(solve(point))