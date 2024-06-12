from sys import stdin
input = lambda:stdin.readline().rstrip()

n = int(input())
l = list(map(int,input().split()))


LIS = [-float("inf")]
for idx in range(n):
    left, right = 0, len(LIS)
    while left<=right:
        middle = (left+right)//2
        if LIS[middle]<=l[idx]:left = middle+1
        else:right = middle-1

    if len(LIS)==middle:LIS.append(l[idx])

f"""
5
5 1 4 2 3

6
10 20 10 30 20 50
"""