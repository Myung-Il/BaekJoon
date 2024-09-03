from sys import stdin, setrecursionlimit
input=lambda:stdin.readline().rstrip()
setrecursionlimit(10**6)


def g(e, bf, bool):
    global l
    s = num[e-1]if bool else 0

    for elm in tree[e]:
        if elm==bf:continue
        if bool:
            s += g(elm, e, False)
        else:
            s += max(g(elm, e, True), g(elm, e, False))
    return s


n = int(input())
num = list(map(int, input().split()))
tree = [[]for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [[0, 0]for _ in range()]
print(g(1, 1, True))