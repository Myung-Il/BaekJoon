import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph,dist = [],[float('inf')] * n
dist[0] = 0

# 그래프 입력
for _ in range(m):
    u,v,w = list(map(int,input().split()))
    graph.append([u-1,v-1,w])

# V-1 번 탐색
for _ in range(n-1):
    for u,v,w in graph:
        if dist[v] > dist[u]+w:
            dist[v] = dist[u]+w

print(dist)
# 음수 사이클 확인
for u,v,w in graph:
    if dist[v] > dist[u]+w:
        print(-1)
        sys.exit()

for i in dist[1:]:
    print(i if i != float('inf') else -1)