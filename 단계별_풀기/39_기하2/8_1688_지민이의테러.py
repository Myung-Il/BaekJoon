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

n = int(input())
protect = [tuple(map(int, input().split()))for _ in range(n)]
people = [tuple(map(int, input().split()))for _ in range(3)]

for human in people:
    count = 0
    for idx in range(-1, n-1):
        first, second = protect[idx], protect[idx+1]
        if not ccw(*first, *second, *human):
            count = 1
            break
        outpoint = 1_000_001, human[1]+1
        count += solve(human, outpoint, first, second)
    if count%2:print(1)
    else:print(0)