import sys
input = sys.stdin.readline
sys.setrecursionlimit(1<<19)

def DFS(now):
  for next in child[now]:
    DFS(next)
    childcnt[now] += childcnt[next]
    result[now] += result[next]+cost[next]*childcnt[next]

def solve(now):
  result[now] = result[parent[now]]+cost[now]*(N-childcnt[now]*2)
  for next in child[now]:
    solve(next)

N = int(input()) # 농장의 수

graph = [[] for i in range(N)] # 트리 그래프
for _ in range(N-1):
  # 노드 연결
  x,y,w = map(int,input().split())
  graph[x-1].append((y-1,w))
  graph[y-1].append((x-1,w))

parent = [0]*N                 # 부모 노드
child = [[] for i in range(N)] # 자식 노드
cost = [0]*N                   # 부모 노드와의 거리
dq = [0]                       # BFS용 덱
while dq:
  now = dq.pop()             # 현재 노드
  for next,w in graph[now]:
    if child[next]: continue # 이미 방문한 노드
    dq.append(next)          # 방문 예정 노드
    child[now].append(next)  # 자식 노드 추가
    parent[next],cost[next] = now,w # 부모 노드, 거리 저장

result = [0]*N
childcnt = [1]*N
DFS(0)
solve(0)
print(*result,sep="\n")