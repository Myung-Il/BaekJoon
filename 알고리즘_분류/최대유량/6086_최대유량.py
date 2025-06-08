from sys import stdin
from collections import defaultdict, deque
from string import ascii_uppercase

input = lambda:stdin.readline().rstrip()
AUP = {ascii:False for ascii in ascii_uppercase}
INF = float("inf")

class EdmondsKarp:
    def __init__(self, G):
        self.graph = G

    def BFS(self, source, sink, parent):
        visit = AUP
        queue = deque()

        visit[source] = True
        queue.append(source)

        while queue:
            vertex = queue.popleft()

            for key in self.graph[vertex]:
                if not visit[key] and self.graph[vertex][key]>0:
                    visit[key] = True
                    queue.append(key)
                    parent[key] = vertex
                    if key==sink:return True
        return False

    
    def maxFlow(self, source, sink):
        parent = AUP
        flow = 0

        while self.BFS(source, sink, parent):
            path = INF
            sk = sink
            while sk!=source:
                path = min(path, self.graph[parent[sk]][sk])
                sk = parent[sk]
        
            flow += path
        
            sk = sink
            while sk!=source:
                vertex = parent[sk]
                self.graph[vertex][sink] -= path
                self.graph[sink][vertex] += path
                sk = parent[vertex]
        return flow

n = int(input())
graph = {ascii2:{ascii1:0 for ascii1 in ascii_uppercase} for ascii2 in ascii_uppercase}
for _ in range(n):
    source, sink, capacity = input().split()
    graph[source][sink] = int(capacity)

EK = EdmondsKarp(graph)

print(EK.maxFlow("A", "Z"))