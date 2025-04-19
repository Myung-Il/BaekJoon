from sys import stdin
import heapq as hq
input = lambda:stdin.readline().rstrip()

n, k, p = map(int, input().split())
check = [1]*k

nums = dict()
for _ in range(p):
    a, b = map(int,input().split())
    if nums.get(b):
        hq.heappush(nums[b], a)
    else:
        check[a] = 0
        nums[b] = []
        hq.heappush(nums[b], a)

print(check)
print(nums)