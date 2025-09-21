from collections import deque
n = int(input())
l = deque()

while n:
    if n%2:l.append(n)
    else:  l.appendleft(n)
    n-=1

print(*l)