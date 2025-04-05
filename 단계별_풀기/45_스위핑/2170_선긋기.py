from sys import stdin
input = lambda:stdin.readline().rstrip()


n = int(input())
l = []
for _ in range(n):
    a, b = map(int,input().split())
    l.append([a, b])
l = sorted(l)

start, end = l[0]
result = 0
for idx in range(1, n):
    a, b = l[idx]
    if end<a:
        result += end-start
        start, end = a, b
    elif end<b:end = b

result += end-start
print(result)