from sys import stdin
input=lambda:stdin.readline().rstrip()

class Point:
    def __init__(self, point):
        self.x, self.y = point
        self.coordinates = (self.x, self.y)

    def __add__(self, point):
        return self.x+point.x, self.y+point.y

    def __sub__(self, point):
        return self.x-point.x, self.y-point.y
    
    def cross(self, point):
        return self.x-point.y, point.x-self.y

    def ccw(self, x1, y1, x2, y2): # 시계방향 : -1, 직선 : 0, 역방향 : 1
        return x1*y2+x2*self.y+self.x*y1 -x2*y1-self.x*y2-x1*self.y

    def distance(self, point): # 점과 점 간의 거리
        x, y = self-point
        return (x**2 + y**2)**0.5
    
    def verticality(self, p1, p2):
        t = p1+self
        return 1.0*abs()

def inner(x1, y1, x2, y2):
    return x1*x2 + y1*y2


def monotoneChain():      # 블록 껍질을 구하는 것 중, x의 정렬만으로 구하는 공식
    upper, lower = [], [] # 윗 집합의 리스트, 아래 집합의 리스트

    for point in points: # lower안의 점이 point보다 왼쪽이거나 직선상에 있으면 꺼낸다, 최외각이 아니기 때문이다.
        while len(lower)>1 and point.ccw(*lower[-2], *lower[-1]) <= 0:lower.pop()
        lower.append(point) # 최외각인 점을 새로 넣어준다
    lower.pop() # 마지막에 추가되는 점은 upper의 시작 점이다.
    
    # x역정렬도 똑같다
    for point in points[::-1]:
        while len(upper)>1 and point.ccw(*upper[-2], *upper[-1]) <= 0:upper.pop()
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
        
        while Point(stack[(right+1)%size]-stack[right%size]+stack[(idx+1)%size]).ccw(stack[idx], stack[(idx+1)%size])>0\
            and inner(stack[(idx+1)%size]-stack[idx], stack[(right+1)%size]-stack[right%size])>0:right+=1
        while Point(stack[(top+1)%size]-stack[top%size]+stack[(idx+1)%size]).ccw(stack[idx], stack[(idx+1)%size])>0:top+=1
        while Point(stack[(left+1)%size]-stack[left%size]+stack[(idx+1)%size]).ccw(stack[idx], stack[(idx+1)%size])>0\
            and inner(stack[(idx+1)%size]-stack[idx], stack[(left+1)%size]-stack[left%size])<0:left+=1
        
        p = stack[(idx+1)%size]-stack[idx]
        result = min(result, )

n = int(input()) # 목장의 수
points = [Point(map(int, input().split()))for _ in range(n)] # 목장의 좌표
points.sort(key=lambda p:(p.x, p.y)) # 블록껍질을 만들기 위한 정렬

# 만약 좌표가 두개면 높이는 없고 너비만 있음 (둘레의 길이를 구해야하니 윗변과 아랫변의 길이를 더해야 함)
if n==2:print(points[0].distance(points[1])*2) # 그래서 *2를 해준다
else:
    stack, cnt = monotoneChain() # 최외각에 있는 점의 스택과 아래 집합의 갯수
    print(rotatingCalipers(stack, cnt)) # 로테이션을 돌본다