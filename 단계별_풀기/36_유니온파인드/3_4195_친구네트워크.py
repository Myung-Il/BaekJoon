from sys import stdin, setrecursionlimit
input = lambda:stdin.readline().rstrip()
setrecursionlimit(10**6)


def union(x, y):
    x, y = find(x), find(y)
    if x==y:return net[x]
    parents[y] = x
    net[x] = net[x]+net[y]
    return net[x]

def find(x):
    if parents[x]!=x:
        parents[x] = find(parents[x])
    return parents[x]


n = int(input())
for _ in range(n):
    m = int(input())
    parents = dict()
    net = dict()
    for _ in range(m):
        a, b = input().split()
        if not parents.get(a):
            parents[a] = a
            net[a] = 1
        if not parents.get(b):
            parents[b] = b
            net[b] = 1

        print(union(a, b))