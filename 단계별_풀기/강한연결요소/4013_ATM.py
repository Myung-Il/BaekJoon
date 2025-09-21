from sys import stdin, setrecursionlimit
from collections import deque
setrecursionlimit(10**6)
input=lambda:stdin.readline().rstrip()


def scc(cur):
    global id, count
    id += 1
    visit[cur] = check = id
    stack.append(cur)
    for nx in graph[cur]:
        if not visit[nx]:check = min(check, scc(nx))
        if visit[nx]:    check = min(check, visit[nx])

    if check==visit[cur]:
        while True:
            node = stack.pop()
            group[node] = count # node가 몇번째 그룹인지 적어둠
            visit[node] = n+1   # 방문 처리
            if cur==node:break
        count += 1 # 그룹의 갯수를 셈
    return check

def bfs(node):              # 시작 그룹 번호
    mx_cost[node] = w[node] # 시작 그룹의 값 총액 설정
    q = deque([node])       # 시작 그룹 다음 그룹을 조회해야 됨
    while q:
        x = q.popleft()                          # q에서 맨앞에 있는 그룹을 가져옴
        for elm in g[x]:                         # 가져온 그룹의 이웃 그룹을 조회
            if mx_cost[elm] < mx_cost[x]+w[elm]: # 다음 그룹의 지금까지의 총액 < 현재 지금까지의 그룹의 총액 + 다음 그룹의 총액
                mx_cost[elm] = mx_cost[x]+w[elm] # 다음 그룹이 지금까지 모은 총액이 적다면 새로 갱신해준다
                q.append(elm)                    # 다음의 다음 그룹을 찾기 위해서 q에 그룹을 추가한다


n, m = map(int,input().split())     # 교차점의 수, 도로의 수
graph = [[]for _ in range(n+1)]     # 를 표현한 그래프
for _ in range(m):                  # 
    a, b = map(int,input().split()) # 교차점 연결
    graph[a].append(b)              # 실질적 연결

cost = [0]                    # 현금 액수를 기록할 리스트
for _ in range(n):            # 
    cost.append(int(input())) # 액수 입력

start, restaurant = map(int,input().split()) # 시작점, 레스토랑의 갯수
rtt = list(map(int,input().split()))         # 레스토랑의 위치

id, count = 0, 0    # 고유값, 그룹의 갯수
visit = [0] * (n+1) # 방문
group = [0] * (n+1) # 어느 그룹에 속했는지
stack = []          # 스택
for elm in range(1, n+1):      #
    if not visit[elm]:scc(elm) # 그룹을 만들어줌

g = [[]for _ in range(count)] # 그룹들의 그래프
w = [0] * count               # 각 그룹들의 총액
mx_cost = [0] * count         # 각 그룹의 총액의 최대를 구할거 bfs에서 자세히
for node in range(1, n+1):
    x = group[node]         # node의 그룹 번호를 받음
    w[x] += cost[node]      # node의 금액을 w(그룹)에 다시 저장
    for elm in graph[node]: # 노드 그래프에서 다음 노드를 받아옴
        y = group[elm]      # 받은 노드의 그룹 번호를 조회
        if x==y:continue    # 같은 그룹이면 패스
        g[x].append(y)      # 다른 그룹이면 그룹끼리 연결
start = group[start]        # 노드 -> 그룹

bfs(start)              # 각 그룹의 최대값 설정
end = [0] * count       # 레스토랑이 있는 그룹을 저장할 리스트
for idx in rtt:         # 낱개로 받음
    end[group[idx]] = 1 # 노드 -> 그룹
    
mx = 0                   # 최대를 저장할 변수
for elm in range(count): # 찾기 시작
    if end[elm]:mx = max(mx, mx_cost[elm])
print(mx)
    

'''
6 7
1 2
2 3
3 5
2 4
4 1
2 6
6 5
10
12
8
16
1
5
1 4
4 3 5 6
'''