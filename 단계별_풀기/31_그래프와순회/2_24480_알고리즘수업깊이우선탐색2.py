from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = lambda:stdin.readline().rstrip()

def dfs(now):
    global deep
    l[now] = sorted(l[now], key=lambda x:x, reverse=True)
    visit[now] = deep
    for elm in l[now]:
        if not visit[elm]:
            deep+=1
            dfs(elm)

deep = 1
n, m, r = map(int,input().split())
l = [[]for _ in range(n+1)]
visit = [0]*(n+1)
for _ in range(m):
    a, b = map(int,input().split())
    l[a].append(b)
    l[b].append(a)

dfs(r)
for idx in range(1, n+1):print(visit[idx])