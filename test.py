from sys import stdin
input = lambda:stdin.readline().rstrip()

def floyd_warshall():
    dist = [[float("inf")]*n for _ in range(n)]
    for s, e, c in graph:
        if dist[s-1][e-1] > c:
            dist[s-1][e-1] = c

    for stopover in range(n):
        for start in range(n):
            for end in range(n):
                path = dist[start][stopover]+dist[stopover][end]
                if dist[start][end] > path:
                    dist[start][end] = path
    return dist

n = int(input())
m = int(input())
graph = [list(map(int,input().split()))for _ in range(m)]

distance = floyd_warshall()
for y in range(n):
    for x in range(n):
        if x==y:distance[y][x] = 0

for lt in distance:
    print(*lt)