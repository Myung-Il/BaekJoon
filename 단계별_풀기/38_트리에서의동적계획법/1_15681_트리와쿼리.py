from sys import stdin, setrecursionlimit
input=lambda:stdin.readline().rstrip()
setrecursionlimit(10**6)


def g(e, bool, bf):
    s = num[e-1]if bool else 0
    for elm in tree[e]:
        if elm==bf:continue
        s += max(g(elm, not bool, e), g(elm, False, e))
    return s


n = int(input())
num = list(map(int, input().split()))
tree = [[]for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

print(max(g(1, True, 1), g(1, False, 1)))