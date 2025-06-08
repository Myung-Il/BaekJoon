from sys import stdin
from collections import defaultdict, deque
from string import ascii_uppercase

input = lambda:stdin.readline().rstrip()
AUP = {ascii:False for ascii in ascii_uppercase}

n = int(input())
graph = defaultdict(dict)
for _ in range(n):
    source, sink, capacity = input().split()
    graph[source][sink] = int(capacity)

for a in graph:
    print(a, graph[a])
    # for b in graph[a]:
    #     print(b, graph[a][b], sep=", ")
    # print()