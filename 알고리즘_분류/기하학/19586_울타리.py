from sys import stdin
input=lambda:stdin.readline().rstrip()

def ccw(x1, y1, x2, y2, x3, y3): # 시계방향 : -1, 직선 : 0, 역방향 : 1
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3

def inner(x1, y1, x2, y2):
    return x1*x2 + y1*y2

def distance(x1, y1, x2, y2): # 점과 점 간의 거리
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def horizontal(x1, y1, x2, y2, x3, y3): # 점1과 2 사이에 3이 내린 수선 발의 좌표
    t = ((x3-x1)*(x2-x1) + (y3-y1)*(y2-y1)) / ((x2-x1)**2 + (y2-y1)**2)
    return (x1 + t*(x2-x1), y1 + t*(y2-y1))

def verticality(x1, y1, x2, y2, x3, y3): # 수선의 발의 좌표에서 3까지의 거리
    if (x2, y2)==(x3, y3)or(x1, y1)==(x2, y2):return 0
    px, py = horizontal(x1, y1, x2, y2, x3, y3)
    return distance(x3, y3, px, py)


def monotoneChain():      # 블록 껍질을 구하는 것 중, x의 정렬만으로 구하는 공식
    upper, lower = [], [] # 윗 집합의 리스트, 아래 집합의 리스트

    for point in points: # lower안의 점이 point보다 왼쪽이거나 직선상에 있으면 꺼낸다, 최외각이 아니기 때문이다.
        while len(lower)>1 and ccw(*lower[-2], *lower[-1], *point) <= 0:lower.pop()
        lower.append(point) # 최외각인 점을 새로 넣어준다
    lower.pop() # 마지막에 추가되는 점은 upper의 시작 점이다.
    
    # x역정렬도 똑같다
    for point in points[::-1]:
        while len(upper)>1 and ccw(*upper[-2], *upper[-1], *point) <= 0:upper.pop()
        upper.append(point)
    upper.pop()
    
    return lower+upper, len(lower)

def rotatingCalipers(stack, num):
    size = len(stack)
    result = float("inf")
    
    right = 1 # 오른쪽 점 번호
    top = 1   #   위쪽 점 번호
    left = 1  #   왼쪽 점 번호
    for idx in range(size):
        # 기준 번호 idx와 같으면 문제가 생김, 피해주는 코드
        if right%size==idx:right+=1
        if  left%size==idx: left+=1
        if   top%size==idx:  top+=1
        
        while ccw(stack[idx], stack[(idx+1)%size], stack[(right+1)%size]-stack[right%size]+stack[(idx+1)%size])\
            and inner(stack[(idx+1)%size]-stack[idx], stack[(right+1)%size]-stack[right%size])


n = int(input()) # 목장의 수
points = [list(map(int, input().split()))for _ in range(n)] # 목장의 좌표
points.sort() # 블록껍질을 만들기 위한 정렬

# 만약 좌표가 두개면 높이는 없고 너비만 있음 (둘레의 길이를 구해야하니 윗변과 아랫변의 길이를 더해야 함)
if n==2:print(distance(*points[0], *points[1])*2) # 그래서 *2를 해준다
else:
    stack, cnt = monotoneChain() # 최외각에 있는 점의 스택과 아래 집합의 갯수
    print(rotatingCalipers(stack, cnt)) # 로테이션을 돌본다