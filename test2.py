from sys import stdin, setrecursionlimit
input=lambda:stdin.readline().rstrip()
setrecursionlimit(10**6)


def g(e, bool, bf):
    s = num[e-1]if bool else 0
    l = [e]if bool else []
    for elm in tree[e]:
        if elm==bf:continue
        a, b = g(elm, not bool, e), g(elm, False, e)
        if a[0]>=b[0]:
            s+=a[0]
            l+=a[1]
        else:
            s+=b[0]
            l+=b[1]
    return s, l


n = int(input())
num = list(map(int, input().split()))
tree = [[]for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

mx, path = max(g(1, True, 1), g(1, False, 1))
print(mx)
print(*sorted(path))