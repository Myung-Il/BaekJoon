import heapq

l = [0, 5, 9, 7, 3, 1]
r = []

for i in l:heapq.heappush(r, i)
for _ in l:print(heapq.heappop(r))