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

for idx in range(n):l[idx].sort()
# 위 과정까지는 별 다를거 없다 굳이 따지면 ans를 추가했다는 것

d = deque([r])      # 방문을 순서대로 해줘야 하기 때문에 큐를 사용
while d:            # 순서대로 받아옴
    x = d.popleft() # 받음
    if visit[x]:continue # 단, 방문한거면 안됨

    # 아래 과정은 각 요소와 연결된 애들 d에 추가하고
    # 방문 처리한거
    ans[x-1] = deep
    visit[x] = 1
    for elm in l[x]:
        if not visit[elm]:
            d.append(elm)
    deep += 1

for elm in ans:print(elm)