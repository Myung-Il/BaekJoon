import heapq
from sys import stdin
input = lambda:stdin.readline().rstrip()

def dijkstra(start):
    h = []
    distance = {i+1:float("inf")for i in range(n)}
    distance[start] = 0
    heapq.heappush(h, [0, start])
    while h:
        cost, now = heapq.heappop(h)
        if distance[now]<cost:continue
        for new, pay in graph[now].items():
            s = pay+cost
            if s<distance[new]:
                distance[new] = s
                heapq.heappush(h, [s, new])
    return distance

for _ in range(int(input())):
    n, m, t = map(int,input().split())
    s, g, h = map(int,input().split())
    graph = {i+1:{}for i in range(n)}
    for _ in range(m):
        a, b, v = map(int,input().split())
        graph[a][b] = v
        graph[b][a] = v
    l = [int(input())for _ in range(t)]

    # 시작과 끝을 입력받는 것보다 마지막 경로가 계속 바뀌는 형태라
    # 재귀를 계속 돌리면서 찾는 것보다 그냥 만들어두고 다시 쓰는게 좋아 보였다
    dijkstraS = dijkstra(s) # 시작에서부터 정점간의 거리
    dijkstraG = dijkstra(g) # 냄새를 맡은 정점에서 거리 1
    dijkstraH = dijkstra(h) # 냄새를 맡은 정점에서 거리 2

    result = []
    for elm in l:
        path1 = dijkstraS[g] + dijkstraG[h] + dijkstraH[elm] # 경로 1
        path2 = dijkstraS[h] + dijkstraH[g] + dijkstraG[elm] # 경로 2
        if path1==dijkstraS[elm]and path1!=float("inf"): result.append(elm)   # INF + INF = INF가 결과 값으로 나올 수 있다고 함
        elif path2==dijkstraS[elm]and path2!=float("inf"): result.append(elm) # 예외 처리해줌
    result.sort()
    print(*result)