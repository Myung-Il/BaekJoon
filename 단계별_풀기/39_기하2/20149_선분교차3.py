from sys import stdin
input=lambda:stdin.readline().rstrip()

def solve():
    if a*b == 0 and c*d == 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return 1
    elif a*b <= 0 and c*d <= 0:return 1
    return 0

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3

def cross():
    px = (a1*b2-b1*a2)*(a3-a4) - (a1-a2)*(a3*b4-b3*a4) # 수학
    py = (a1*b2-b1*a2)*(b3-b4) - (b1-b2)*(a3*b4-b3*a4) # 적인
    p =  (a1-a2)*(b3-b4) - (b1-b2)*(a3-a4)             # 공식
    try:print(px/p, py/p)                              # p가 0이 나오면 두 선분은 겹침
    except:
        point = [(a1, b1), (a2, b2), (a3, b3), (a4, b4)]             # 점 선분에서 어떤게 겹치고 얼마나 겹치는지 확인
        if point[0]>point[1]:point[0], point[1] = point[1], point[0] # 범위를 측정하기 위해서 순서를 정리해준다
        if point[2]>point[3]:point[2], point[3] = point[3], point[2] # 작은게 아래로 가게 하여서 한점만 만나는지 검사한다
        if   point[0]==point[3]:print(*point[0])                     # 0--1,2--3 식인지 2--3,0--1 식으로 연결되어 있는지보고
        elif point[1]==point[2]:print(*point[1])                     # 0--2--1,3 처럼 겹치는 것은 넘겨버린다


a1, b1, a2, b2 = map(int,input().split())
a3, b3, a4, b4 = map(int,input().split())

mx1, my1, mx2, my2 = min(a1, a2), min(b1, b2), max(a1, a2), max(b1, b2)
mx3, my3, mx4, my4 = min(a3, a4), min(b3, b4), max(a3, a4), max(b3, b4)

a = ccw(a1, b1, a2, b2, a3, b3)
b = ccw(a1, b1, a2, b2, a4, b4)
c = ccw(a3, b3, a4, b4, a1, b1)
d = ccw(a3, b3, a4, b4, a2, b2)

result = solve()  # 교점이 있는지 확인
print(result)     # 결과 도출
if result:cross() # 교점이 있다면 교점 찾으러 출발