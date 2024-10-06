import heapq as hq
from sys import stdin
input = lambda:stdin.readline().rstrip()

n,k = map(int,input().split())
v = [0]*(n+1)
d = {i+1:[]for i in range(n)}
for i in range(k):
    fst,sec = map(int,input().split())
    d[fst].append(sec)
    v[sec]+=1

q = []
for i in range(n):
    if v[i+1]==0:hq.heappush(q,i+1)

r = []
while q:
    x = hq.heappop(q)
    r.append(x)

    for i in d[x]:
        v[i] -= 1
        if v[i]==0:hq.heappush(q,i)
    
print(*r)