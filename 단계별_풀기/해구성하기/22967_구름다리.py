from sys import stdin
input = lambda:stdin.readline().strip()

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

if n==2:
    print(0)
    print(1)
elif n==3:
    print(1)
    print(1)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if j in graph[i]:continue
            print(i, j)
elif n==4:
    print(n-1)
    print(1)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if j in graph[i]:continue
            print(i, j)
else:
    node, length = 0, 0
    for i in range(n+1):
        if len(graph[i]) > length:
            node = i
            length = len(graph[i])

    print(n-length-1)
    print(2)
    for i in range(1, n+1):
        if i in graph[node] or i==node:continue
        print(node, i)