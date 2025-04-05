from collections import deque

n = int(input())
d = {i+1:[]for i in range(n)}
for _ in range(n-1):
    a, b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)
visit = [0]*(n+1)
result = [0]*(n+1)

q = deque()
q.append(1)
while q:
    x = q.popleft()
    visit[x] = 1
    for elm in d[x]:
        if visit[elm]:continue
        q.append(elm)
        result[elm] = x

for idx in range(1, n):
    print(result[idx+1])