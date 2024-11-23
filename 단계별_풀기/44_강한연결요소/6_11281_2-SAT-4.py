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

for elm in range(-n, n+1):
    if not elm:continue
    if not visit[elm]:scc(elm)

result = [0] * n
for idx in range(1, n+1):
    if group[idx]==group[-idx]:
        print(0)
        break
    if group[idx] < group[-idx]:
        result[idx-1] = 1
else:
    print(1)
    print(*result)