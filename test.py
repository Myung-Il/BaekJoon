from sys import stdin
input=lambda:stdin.readline().rstrip()

class Operation:
    def __add__(p1, p2):return Point(p1.x+p2.x, p1.y+p2.y)
    def __sub__(p1, p2):return Point(p1.x-p2.x, p1.y-p2.y)

class Point(Operation):
    def __init__(self, X, Y):
        self.x, self.y = X, Y
        self.coordinates = X, Y
    
    def __iter__(self):
        yield self.x
        yield self.y


def ccw(x1, y1, x2, y2, x3, y3): # 시계방향 : -1, 직선 : 0, 역방향 : 1
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3

def  dot(p1, p2) :return p1.x*p2.x +p1.y*p2.y
def cross(p1, p2):return p1.x*p2.y +p2.x*p1.y

def distance(A, B):
    x, y = A - B
    return (x**2 + y**2)**0.5

def distance2(A, B, C):
    T = Point(*(A+C))
    return 1.0 * abs(cross((B-A), (T-A))) / distance(A, T)


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
    
    return lower+upper

def rotatingCalipers(stk):
    size = len(stk)
    result = float("inf")
    
    j = k = l = 1
    for i in range(size):
        a = stk[i]
        b = stk[(i + 1) % size]
        edge = b - a
        edge_len = (edge.x ** 2 + edge.y ** 2) ** 0.5
        ux, uy = edge.x / edge_len, edge.y / edge_len  # 단위 벡터

        max_proj, min_proj = -float("inf"), float("inf")
        max_ortho, min_ortho = -float("inf"), float("inf")

        for p in stk:
            dx = p.x - a.x
            dy = p.y - a.y
            # edge 방향으로의 투영
            proj = dx * ux + dy * uy
            # edge에 수직한 방향으로의 투영
            ortho = -dx * uy + dy * ux

            max_proj = max(max_proj, proj)
            min_proj = min(min_proj, proj)
            max_ortho = max(max_ortho, ortho)
            min_ortho = min(min_ortho, ortho)

        width = max_proj - min_proj
        height = max_ortho - min_ortho
        result = min(result, 2 * (width + height))

    return result


n = int(input())
points = [Point(*map(int, input().split()))for _ in range(n)]
points.sort(key=lambda p:(p.x, p.y))

if n==2:print(distance(points[0], points[1])*2)
else:
    stack = monotoneChain()
    print(rotatingCalipers(stack))