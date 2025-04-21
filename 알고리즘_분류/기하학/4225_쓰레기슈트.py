from sys import stdin
import math
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

def angle(ax, ay, bx, by, cx, cy):
    bax, bay = ax-bx, ay-by # 벡터 BA
    bcx, bcy = cx-bx, cy-by # 벡터 BC

    # 내적과 외적
    dot = bax*bcx + bay*bcy
    det = bax*bcy - bay*bcx

    theta_rad = math.atan2(-det, dot)
    theta_deg = math.degrees(theta_rad)
    return theta_deg % 360

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

            if angle(*p1, *p2, *p3)>90:continue
            length = max(length, height(*p3, *p1, *p2))
        result = min(result, length)
    
    print(f"Case {turn}: {ceil2(result):0.2f}")