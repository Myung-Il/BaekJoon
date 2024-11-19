import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def DFS(now):
    global id
    stack.append(now)
    visited[now] = nowid = id
    for next in graph[now]:
        if not visited[next]:
            id += 1
            DFS(next)
        if visited[next] <= nowid:
            indegree[next] -= 1
            visited[now] = min(visited[now],visited[next])
            print(now+1, "===", next+1)
    if visited[now] == nowid:
        scc.append([]); sccindegree.append(0)
        while 1:
            x = stack.pop()
            scc[-1].append(x)
            sccindegree[-1] += indegree[x]
            visited[x] = 1e7
            if x == now:
                break
        print(now, indegree, sccindegree)
        
for _ in range(int(input())):
    N,M = map(int,input().split())
    
    graph = [[] for i in range(N)]; indegree = [0]*N
    for _ in range(M):
        a,b = map(int,input().split())
        graph[a-1].append(b-1)
        indegree[b-1] += 1
    
    visited = [0]*N
    stack,scc,sccindegree = [],[],[]
    for i in range(N):
        if not visited[i]:
            id = 1
            DFS(i)
    print(sccindegree.count(0))