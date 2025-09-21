from sys import stdin, setrecursionlimit
setrecursionlimit(10**5) # 메모리 용량 늘려줌
input = lambda:stdin.readline().rstrip()
# 메모리 초과가 심각함

def dfs(now):
    global deep
    l[now].sort()
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
    # l[a][b], l[b][a] = 1, 1
    # 위 처럼 했다가 메모리 초과가 뜸 리스트 크기가 40,000,000,000이긴 했음
    # 지금은 필요한 만큼만 만들어줌

dfs(r)
for idx in range(1, n+1):print(visit[idx])