from sys import stdin
input = lambda:stdin.readline().rstrip()

def floyd_warshall():
    dist = [[INF for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]
            road[i][j] = [i+1, j+1] # 시작 위치와 도착 위치 기록
        dist[i][i] = 0   # 제자리 이동은 없으니 0
        road[i][i] = [0] # 움직이지를 않았으니 0

    for k in range(n):         # 거쳐가는 점
        for i in range(n):     # 시작하는 점
            for j in range(n): # 도착지는 점
                if dist[i][j] > dist[i][k] + dist[k][j]: # 그냥 갔을 때랑 거쳐서 갔을 때 비교
                    dist[i][j] = dist[i][k] + dist[k][j] # 거쳐서가는게 더 빠르면 갱신
                    road[i][j] = road[i][k] + road[k][j][1:] # 거쳐갔으니 이전 들렀던 위치들과 
                                                             # 도착 위치까지의 과정 위치들을 갱신

    for i in range(n):
        for j in range(n):
            if INF==dist[i][j]:  # 갈 수 없을때
                dist[i][j] = 0   # 0으로 출력하라고 함
                road[i][j] = [0] # 못 갔으니 들른 장소도 0개
    return dist, road

INF = float('inf')
n = int(input())
m = int(input())
graph = [[INF]*n for _ in range(n)]
road = [[0]*n for _ in range(n)] # 어떤 길을 통해서 돌아봤는지 알아야하기 때문에 필요함
for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)

cost, way = floyd_warshall()
for i in cost:print(*i)
for i in range(n):
    for j in range(n):
        if way[i][j][0]:print(len(way[i][j]), *way[i][j])
        else:print(0)