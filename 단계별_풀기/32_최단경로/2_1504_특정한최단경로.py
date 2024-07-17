import heapq
from sys import stdin
input = lambda:stdin.readline().rstrip()

def dijkstra(start, end):
    h = [] # 힙 트리
    distance = {i+1:float("inf")for i in range(n)} # start에서 갈 수 있는 거리
    distance[start] = 0           # 본인으로 가기위한 비용은 0
    heapq.heappush(h, [0, start]) # 비용과 지금 위치 저장
    while h:
        cost, now = heapq.heappop(h)      # 비용과 지금 위치

        if distance[now]<cost:continue    # 기존 거리와 새로 찾은 거리를 비교
                                          # 새로 찾은게 더 짧으면 탐색을 해봄
        for new, price in g[now].items(): # 다음 위치와 다음 위치로 가기 위한 비용
            s = cost+price        # 새로 찾은 거리와 다음 위치로 가기위한 비용이
            if s<distance[new]:   # 기존의 비용보다 작아야지만
                distance[new] = s # 기록해줌, 그리고 저장
                heapq.heappush(h, [s, new])
    return distance[end] # start에서 end까지의 비용 반환


n, m = map(int,input().split())
g = {i+1:{}for i in range(n)}
for _ in range(m):
    a, b, v = map(int,input().split())
    g[a][b] = v
    g[b][a] = v
v1, v2 = map(int,input().split())

middle = dijkstra(v1, v2) # v1 -> v2,  v2 -> v1 두 방법의 길이는 모두 같음
sol1 = dijkstra(1, v1) + middle + dijkstra(v2, n) # 과정을 끊어서 확인
sol2 = dijkstra(1, v2) + middle + dijkstra(v1, n) # v1을 먼저가는 경우와 v2를 먼저가는 경우 2개
sol3 = dijkstra(1, n)if (v1==1 and v2==n)or(v1==n and v2==1)else float("inf") # v1과 v2가 각각 시작과 끝일 때
mn = min(sol1, sol2, sol3)
print(mn if mn<float("inf")else -1)