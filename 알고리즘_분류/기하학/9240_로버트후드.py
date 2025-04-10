from sys import stdin
import math
import heapq as hq
input=lambda:stdin.readline().rstrip()
INF = float("inf")

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3

def angle(ax, ay, bx, by, cx, cy):
    bax, bay = ax-bx, ay-by # 벡터 BA
    bcx, bcy = cx-bx, cy-by # 벡터 BC

    # 내적과 외적
    dot = bax*bcx + bay*bcy
    det = bax*bcy - bay*bcx

    theta_rad = math.atan2(-det, dot)
    theta_deg = math.degrees(theta_rad)
    return theta_deg % 360

def length(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


def convexHull():         # 볼록 껍질 함수
    stack, queue = [], [] # 시작점을 기준으로 점들 스택, 세점이 이루는 각도 큐
    x, y = points[0]      # 시작 점

    for point in points[1:]:                                     # 세 좌표 간의 각도를 계산하고
        hq.heappush(queue, (angle(*point, x, y, x+1, y), point)) # 힙 트리로 순서를 만듬
    stack.append((x, y))               # 스택에 첫 점을 넣고
    stack.append(hq.heappop(queue)[1]) # ccw를 하기 위해서 다음 점을 찾아서 넣음

    firstpoint, secondpoint = 0, 1
    for _ in range(n-2):                  # 모든 점들을 확인 함
        thirdpoint = hq.heappop(queue)[1] # ccw를 하기 위해서 점 3개가 필요하고
        res = ccw(*stack[firstpoint], *stack[secondpoint], *thirdpoint) # 방향 확인

        if res>0:
            stack.append(thirdpoint) # 시계 방향이면 스택에 추가
            firstpoint  += 1
            secondpoint += 1
        else:                        # 반 시계 방향이면
            stack.pop()              # 저장한 점을 꺼내고
            stack.append(thirdpoint) # 새로운 점을 추가
            
    return stack # 이 과정을 거치면 stack에는 점들로 만들 도형이 하나 만들어짐

def rotatingCalipers(stack):
    stksize = len(stack)
    if stksize==2:return length(*stack[0], *stack[1])

    mxlength = 0      # 두 좌표 사이의 최대 길이
    i, j = 1, 2       # 0번째부터 시작하는 각 선분의 마지막 위치
    while stksize!=i: # 시작 선이 아직 한바퀴를 덜 돌았다면
        j %= stksize
        a, b = stack[i-1], stack[i]
        c, d = stack[j-1], stack[j]

        diff = (b[0]-c[0], b[1]-c[1])    # 두 선분과의 거리
        c = (c[0]+diff[0], c[1]+diff[1]) # 두 좌표 연결
        d = (d[0]+diff[0], d[1]+diff[1])

        mxlength = max(mxlength, length(*a, *d)) # 최대 길이 설정
        if i!=j+1 and ccw(*a, *b, *d): j += 1 # 선분이 나아간다면
        else:                          i += 1 # 선분이 돌아온다면
    return mxlength


n = int(input())
points = [tuple(map(int,input().split()))for _ in range(n)]
points.sort(key=lambda pos:(pos[1], pos[0]))

con = convexHull()
rot = rotatingCalipers(con)
print(rot)