from sys import stdin
from collections import defaultdict, deque
from string import ascii_uppercase

input = lambda:stdin.readline().rstrip()
INF = float("inf")

class EdmondsKarp:
    def __init__(self, G):
        self.graph = G

    def BFS(self, source, sink, parent):
        visit = defaultdict(bool)
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
        parent = dict()
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
                self.graph[vertex][sk] -= path
                self.graph[sk][vertex] += path
                sk = vertex
        return flow

n = int(input())
graph = defaultdict(lambda:defaultdict(int))
for _ in range(n):
    source, sink, capacity = input().split()
    graph[source][sink] += int(capacity)
    graph[sink][source] += int(capacity)

EK = EdmondsKarp(graph)

print(EK.maxFlow("A", "Z"))