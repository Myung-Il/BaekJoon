from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)
input = lambda:stdin.readline().rstrip()

def dfs(now):
    global deep
    for elm in range(1, n+1):
        if l[now][elm] and not visit[elm]:
            deep+=1
            visit[elm] = deep
            dfs(elm)

n, m, r = map(int,input().split())
l = [[0]*(n+1)for _ in range(n+1)]
visit = [0]*(n+1)
for _ in range(m):
    a, b = map(int,input().split())
    l[a][b], l[b][a] = 1, 1

deep = 1
visit[r] = deep
dfs(r)

for idx in range(1, n+1):print(visit[idx])