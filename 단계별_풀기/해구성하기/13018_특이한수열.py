from sys import stdin
input = lambda:stdin.readline().strip()

n, k = map(int, input().split())

if n==1:print("Impossible")
else:
    for i in range(2, n-k+1):print(i, end=' ')
    print(1, end=' ')
    for i in range(n-k+1, n+1):print(i, end=' ')