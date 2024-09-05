from sys import stdin
input=lambda:stdin.readline().rstrip()

def solve():
    if a*b == 0 and c*d == 0: # 평행할 때
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return 1 # 두 점 중 하나의 x값과 y값은 선분 L1 범위안에 있어야 한다
    else:
        if a*b <= 0 and c*d <= 0:
            return 1

    return 0

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3


a1, b1, a2, b2 = map(int,input().split()) # 선분 L1 위의 두 점
a3, b3, a4, b4 = map(int,input().split()) # 선분 L2 위의 두 점

# 두 선분이 평행할 때, 교차하는지 알기 위한 각 x,y에서 최소와 최대를 구한다
mx1, my1, mx2, my2 = min(a1, a2), min(b1, b2), max(a1, a2), max(b1, b2)
mx3, my3, mx4, my4 = min(a3, a4), min(b3, b4), max(a3, a4), max(b3, b4)

a = ccw(a1, b1, a2, b2, a3, b3) # 선분 L1에 대해 점3이 어디에 있는지 확인
b = ccw(a1, b1, a2, b2, a4, b4) # 선분 L1에 대해 점4가 어디에 있는지 확인
c = ccw(a3, b3, a4, b4, a1, b1) # 선분 L2에 대해 점1이 어디에 있는지 확인
d = ccw(a3, b3, a4, b4, a2, b2) # 선분 L2에 대해 점2가 어디에 있는지 확인

print(solve())