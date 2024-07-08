from sys import stdin
input = lambda:stdin.readline().rstrip()

for _ in range(int(int(input()))):
    n = int(input())
    l = list(map(int,input().split()))
    k = list([0]*n for _ in range(n))

    for idx in range(1, n):
        k[idx-1][idx] = l[idx-1]+l[idx]
        for x in range(idx+1, n):
            k[idx-1][x] = k[idx-1][x-1]+l[x]

    for x in range(2, n):
        for y in range(n-x):
            k[y][x+y] += min([k[y][idx]+k[idx+1][x+y] for idx in range(y, x+y)])

    print(k[0][-1])