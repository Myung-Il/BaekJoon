from sys import stdin
from collections import deque as dq
input = lambda:stdin.readline().strip()

n = int(input())
farm = dq([int(input())for _ in range(n)])

result = 0
for day in range(1, n+1):
    if farm[0] < farm[-1]:
        result += day*farm.popleft()
    else:result += day*farm.pop()

print(result)