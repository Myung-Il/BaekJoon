from test import txt

from sys import stdin
input=lambda:stdin.readline().rstrip()

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3

def solve(point1, point2, point3, point4):
    x1, y1, x2, y2 = *point1, *point2
    x3, y3, x4, y4 = *point3, *point4

    # 두 선분이 평행할 때, 교차하는지 알기 위한 각 x,y에서 최소와 최대를 구한다
    mx1, my1, mx2, my2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
    mx3, my3, mx4, my4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)

    a = ccw(x1, y1, x2, y2, x3, y3) # 선분 L1에 대해 점3이 어디에 있는지 확인
    b = ccw(x1, y1, x2, y2, x4, y4) # 선분 L1에 대해 점4가 어디에 있는지 확인
    c = ccw(x3, y3, x4, y4, x1, y1) # 선분 L2에 대해 점1이 어디에 있는지 확인
    d = ccw(x3, y3, x4, y4, x2, y2) # 선분 L2에 대해 점2가 어디에 있는지 확인

    if a*b == 0 and c*d == 0: # 평행할 때
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:return 1
    elif a*b <= 0 and c*d <= 0:return 1
    return 0

def cross(point1, point2, point3, point4):
    x1, y1, x2, y2 = *point1, *point2
    x3, y3, x4, y4 = *point3, *point4

    px = (x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4) # 수학
    py = (x1*y2-y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4) # 적인
    p =  (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)             # 공식
    try:return (px/p, py/p)                            # p가 0이 나오면 두 선분은 겹침
    except:
        point = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]             # 점 선분에서 어떤게 겹치고 얼마나 겹치는지 확인
        if point[0]>point[1]:point[0], point[1] = point[1], point[0] # 범위를 측정하기 위해서 순서를 정리해준다
        if point[2]>point[3]:point[2], point[3] = point[3], point[2] # 작은게 아래로 가게 하여서 한점만 만나는지 검사한다
        if   point[0]==point[3]:return point[0]                      # 0--1,2--3 식인지 2--3,0--1 식으로 연결되어 있는지보고
        elif point[1]==point[2]:return point[1]                      # 0--2--1,3 처럼 겹치는 것은 넘겨버린다

examples = txt.strip().split("\n\n")
for i, example in enumerate(examples, 1):
    ex = example.split("\n")
    result = []

    n = int(ex[0])
    protect = [tuple(map(int, ex[idx].split()))for idx in range(1, n+1)]
    people = [tuple(map(int, ex[idx].split()))for idx in range(n+1, n+4)]
    res = [int(ex[idx]) for idx in range(n+4, n+7)]

    for human in people:
        count = 0
        for idx in range(-1, n-1):
            first, second = protect[idx], protect[idx+1]
            outpoint = 1_000_001, human[1]+1
            r = solve(human, outpoint, first, second)

            if r and cross(human, outpoint, first, second)==human:
                count=1
                break
            count += r
        if count%2:result.append(1)
        else:result.append(0)
        
    if result!=res:print(ex, result)