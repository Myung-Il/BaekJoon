from sys import stdin
input=lambda:stdin.readline().rstrip()

class Operation:
    def __add__(p1, p2):return p1.x+p2.x, p1.y+p2.y
    def __sub__(p1, p2):return p1.x-p2.x, p1.y-p2.y

class Point(Operation):
    def __init__(self, point):
        self.x, self.y = point

    def __iter__(self):
        yield self.x
        yield self.y

    def ccw(self, x1, y1, x2, y2): # 시계방향 : -1, 직선 : 0, 역방향 : 1
        return x1*y2+x2*self.y+self.x*y1 -x2*y1-self.x*y2-x1*self.y

    def distance(self, point):
        x, y = self-point
        return (x**2 + y**2)**0.5
    
    
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
    
    return lower+upper


n = int(input())
points = [Point(map(int, input().split()))for _ in range(n)]
points.sort(key=lambda p:(p.x, p.y))

stack = monotoneChain()
print(len(stack))
print(Point(stack[0]+stack[1]).distance(stack[2]))