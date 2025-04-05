from sys import stdin
input = lambda:stdin.readline().rstrip()

def floyd_warshall(dist):
    for stopover in range(n):
        for start in range(n):
            for end in range(n):
                path = dist[start][stopover]+dist[stopover][end]
                if dist[start][end] > path:
                    dist[start][end] = path
    return dist

n, m = map(int,input().split())
graph = [[float("inf")]*n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a-1][b-1] = c

li = floyd_warshall(graph)
result = min([li[i][i]for i in range(n)])    # 왕복이라고 했으니 본인 위치가
print(-1 if result==float("inf")else result) # 갱신되어 있다면 갔다온 것이다