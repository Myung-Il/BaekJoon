from sys import stdin
import heapq as hq
from collections import deque
input = lambda:stdin.readline().rstrip()

def topologySort(type):
    check = [1]*k

    degree = dict()
    nums = dict()

    topology = []
    for a, b in load:
        # 위상 정렬
        # 가는 방향
        if degree.get(a):
            hq.heappush(degree[a], b*type)
        else:
            degree[a] = []
            hq.heappush(degree[a], b*type)

        # 받는 방향
        if nums.get(b):
            hq.heappush(nums[b], a*type)
        else:
            check[b] = 0
            nums[b] = []
            hq.heappush(nums[b], a*type)

    for idx in range(k):
        if check[idx]:
            group = []
            queue = deque()
            queue.append(idx)
            while queue:
                x = queue.popleft()
                group.append(x)
                if not degree.get(x):continue
                for elm in degree[x]:
                    hq.heappop(nums[elm])
                    if not nums[elm]:queue.append(elm)
            topology.append(group)
    return topology, type

def solve(list, diff):
    result = 0
    order = k-1
    for group in list:
        for elm in group:
            result += (elm+diff)*n**order
            order -= 1
    return result

n, k, p = map(int, input().split())
load = list(map(int, input().split()))

print(solve(topologySort(1)))
print(solve(topologySort(-1)))