from sys import stdin
input = lambda:stdin.readline().rstrip()

def floyd_warshall(dist):
    for stopover in range(n):    # 경유지 설정
        for start in range(n):   # 출발지 설정
            for end in range(n): # 도착지 설정
                path = dist[start][stopover]+dist[stopover][end]
                if dist[start][end] > path:
                    dist[start][end] = path
    return dist

n = int(input())
m = int(input())
graph = [[float("inf")]*n for _ in range(n)] # 일단 모든 경로가 무한대임, 아직 모르니까
for i in range(n):graph[i][i] = 0            # 본인 위치는 0
for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c) # 중복도 있으니 가장 작은 걸로 갱신

distance = floyd_warshall(graph)
for y in range(n):
    for x in range(n):
        if distance[y][x]==float("inf"): # 100,001보다 작아야 하는데
            distance[y][x] = 0 # 이 과정이 없으면 작은 것을 확인하지 못하고 넘어감
            
for lt in distance:
    print(*lt)