from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input=lambda:stdin.readline().rstrip()


def scc(cur):
    global id, count
    id += 1
    visit[cur] = check = id
    stack.append(cur)
    for nx in graph[cur]:
        if not visit[nx]:check = min(check, scc(nx))
        if visit[nx]:    check = min(check, visit[nx])

    if check==visit[cur]:
        while True:
            node = stack.pop()
            visit[node] = n*2
            group[node] = count
            if cur==node:break
        count += 1
    return check


n, m = map(int,input().split())
graph = [[]for _ in range(n*2+1)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[-a].append(b)
    graph[-b].append(a)

id, count = 0, 1
visit = [0] * (n*2+1)
group = [0] * (n*2+1)
stack = []

for elm in range(1, n*2+1):
    if not visit[elm]:scc(elm)

for idx in range(1, n+1):
    if group[idx]==group[-idx]:
        print(0)
        break
else:print(1)