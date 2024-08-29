from sys import stdin, setrecursionlimit
input = lambda:stdin.readline().rstrip()
setrecursionlimit(10**6)


def union(x, y, i):
    global result, flag
    x, y = find(x), find(y)
    if x==y:
        result = i+1
        flag = False
    if x<y:parents[y] = x
    else:  parents[x] = y

def find(x):
    if parents[x]!=x:
        parents[x] = find(parents[x])
    return parents[x]


n, m = map(int,input().split())
parents = [idx for idx in range(n)]
flag, result = True, 0
for idx in range(m):
    a, b = map(int,input().split())
    if flag:union(a, b, idx)
print(result)