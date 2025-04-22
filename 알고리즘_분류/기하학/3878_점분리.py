from sys import stdin
import math
input=lambda:stdin.readline().rstrip()

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3

def length(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def pointSort(p1, p2):
    return *min(p1, p2), *max(p1, p2)


def monotoneChain(points):
    if len(points)==1:return points

    points.sort()
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

def check3(point1, point2, mpoint):
    if not ccw(*point1, *point2, *mpoint):
        px1, py1, px2, py2 = pointSort(point1, point2)
        mpx, mpy = mpoint
        if px1<=mpx<=px2 and py1<=mpy<=py2:return True
    return False

def check4(bpoint1, bpoint2, wpoint1, wpoint2):
    a = ccw(*bpoint1, *bpoint2, *wpoint1)
    b = ccw(*bpoint1, *bpoint2, *wpoint2)
    c = ccw(*wpoint1, *wpoint2, *bpoint1)
    d = ccw(*wpoint1, *wpoint2, *bpoint2)

    if a*b==0 and c*d==0:
        bx1, by1, bx2, by2 = pointSort(bpoint1, bpoint2)
        wx1, wy1, wx2, wy2 = pointSort(wpoint1, wpoint2)
        if bx1 <= wx2 and wx1 <= bx2 and by1 <= wy2 and wy1 <= by2:
            return True
    elif a*b<=0 and c*d<=0: return True
    return False

def solve():
    # 영역 하나가 잡아 먹은 경우
    if stack==black or stack==white:return False

    # 영역이 1개씩 밖에 없어서 구분이 되는 경우
    elif bsize==1 and wsize==1:return True

    # 영역 하나가 1개 밖에 없어서 선 위에 있는 확인해야 되는 경우
    elif bsize==1:
        for idx in range(1, wsize+1):
            p1 = white[(idx-1)%wsize]
            p2 = white[idx%wsize]
            if check3(p1, p2, black[0]):return False
    elif wsize==1:
        for idx in range(1, bsize+1):
            p1 = black[(idx-1)%bsize]
            p2 = black[idx%bsize]
            if check3(p1, p2, white[0]):return False
    
    # 영역이 넓어서 겹치는지 일일히 확인해야 되는 경우
    else:
        for idx in range(1, wsize+1):
            p1 = white[(idx-1)%wsize]
            p2 = white[idx%wsize]
            for idx in range(1, bsize+1):
                p3 = black[(idx-1)%bsize]
                p4 = black[idx%bsize]
                if check4(p1, p2, p3, p4):return False

    # 그 어떤 경우에도 포함 되지 않을 때
    return True


for _ in range(int(input())):
    b, w = map(int, input().split())
    black = monotoneChain([list(map(int, input().split()))for _ in range(b)])
    white = monotoneChain([list(map(int, input().split()))for _ in range(w)])
    stack = monotoneChain(black+white)

    bsize = len(black)
    wsize = len(white)

    if solve():print("YES")
    else:      print("NO")