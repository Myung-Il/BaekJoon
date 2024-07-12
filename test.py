import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(value):
    global cnt
    visited[value] = cnt    
    for v in A[value]:
        if visited[v] == 0:
            cnt += 1
            dfs(v)

cnt = 1
N, M, R = map(int, input().split())
A = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)    
    A[s].sort()
dfs(R)

for _ in range(1, N+1):print(visited[_])