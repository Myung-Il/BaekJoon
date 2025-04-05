from collections import deque
from sys import stdin
input = lambda:stdin.readline().rstrip()

deep = 1
n, m, r = map(int,input().split())
l = [[]for _ in range(n+1)]
visit = [0]*(n+1)
ans = [0]*n
for _ in range(m):
    a, b = map(int,input().split())
    l[a].append(b)
    l[b].append(a)

d = deque([r])
while d:
    x = d.popleft()
    if visit[x]:continue

    ans[x-1] = deep
    visit[x] = 1
    l[x].sort(reverse=True) # 자리만 옮김
    for elm in l[x]:
        if not visit[elm]:
            d.append(elm)
    deep += 1

for elm in ans:print(elm)