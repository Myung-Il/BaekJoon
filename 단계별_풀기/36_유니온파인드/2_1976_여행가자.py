from sys import stdin, setrecursionlimit
input = lambda:stdin.readline().rstrip()
setrecursionlimit(10**6)


def union(x, y):
    x, y = find(x), find(y)
    if x<y:parents[y] = x
    else:  parents[x] = y

def find(x):
    if parents[x]!=x:
        parents[x] = find(parents[x])
    return parents[x]


n = int(input())
m = int(input())
parents = [num for num in range(n+1)]
for i in range(n):
    l = list(map(int,input().split()))
    for j in range(n):
        if i==j or not l[j]:continue
        union(i+1, j+1)
    find(i+1)

result = set()
for elm in map(int,input().split()):
    result.add(parents[elm])

print("YES"if len(result)==1 else"NO")