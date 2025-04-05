from sys import stdin
import math
import heapq as hq
input=lambda:stdin.readline().rstrip()

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3

def angle(x1, y1, x2, y2): # 인터넷에 떠도는 각도 구하는 코드
    if y1==y2:return 0
    if x1==x2:return 0

    x3, y3 = x2, y1
    BA = (x2 - x1, y2 - y1)
    BC = (x3 - x1, y3 - y1)
    
    dot_product = BA[0]*BC[0] + BA[1]*BC[1] # 내적
    
    mag_BA = math.sqrt(BA[0]**2 + BA[1]**2) # 벡터 크기
    mag_BC = math.sqrt(BC[0]**2 + BC[1]**2)
    
    cos_theta = dot_product / (mag_BA * mag_BC) # 코사인 각도
    cos_theta = max(-1.0, min(1.0, cos_theta))  # 소수점 계산 오차 방지
    
    angle_rad = math.acos(cos_theta) # 라디안
    return math.degrees(angle_rad)   # 변환 도(degree)

def graham(type):               # 볼록 껍질 함수
    stack, queue = [], []       # 시작점을 기준으로 점들 스택, 세점이 이루는 각도 큐
    points = protect[:]         # 기본적인 점들
    match type:                 # 테두리 점을 구할 때, 사람이 포함되는가 아닌가
        case 1:points.append(people[0]) # 대연이 좌표 추가
        case 2:points.append(people[1]) # 영훈이 좌표 추가
        case 3:points.append(people[2]) # 범진이 좌표 추가
    firstpoint = sorted(points, key=lambda x:(x[1], x[0]))[0] # 첫 점

    for point in points[1:]:                                    # 세 좌표 간의 각도를 계산하고
        hq.heappush(queue, (angle(*firstpoint, *point), point)) # 힙 트리로 순서를 만듬
    stack.append(firstpoint)           # 스택에 첫 점을 넣고
    stack.append(hq.heappop(queue)[1]) # ccw를 하기 위해서 다음 점을 찾아서 넣음
    
    firstpoint, secondpoint = 0, 1
    for _ in range(len(points)-2):      # 모든 점들을 확인 함
        thirdpoint = hq.heappop(queue)[1] # ccw를 하기 위해서 점 3개가 필요하고
        res = ccw(*stack[firstpoint], *stack[secondpoint], *thirdpoint) # 방향 확인
        if res>0:
            stack.append(thirdpoint)      # 시계 방향이면 스택에 추가
            firstpoint  += 1
            secondpoint += 1
        else:                             # 반 시계 방향이면
            stack.pop()                   # 저장한 점을 꺼내고
            stack.append(thirdpoint)      # 새로운 점을 추가
            
    return stack # 이 과정을 거치면 stack에는 점들로 만들 도형이 하나 만들어짐

def area(stack):
    mainpoint = stack[0]
    areasize = 0
    for idx in range(1, len(stack)-1):
        areasize += ccw(*mainpoint, *stack[idx], *stack[idx+1])/2

    return areasize



n = int(input())
protect = [tuple(map(int, input().split()))for _ in range(n)]
people = [tuple(map(int, input().split()))for _ in range(3)]

basicsarea = area(graham(0))
for idx in range(3):
    if basicsarea==area(graham(idx+1)):print(1)
    else:print(0)