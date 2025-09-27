from sys import stdin
input = lambda:stdin.readline().strip()

n = int(input())
arr = [i for i in range(2001)]

point = 1
res = 0
while True:
    res += arr[point]
    if res > n:
        print(point-1)
        break
    elif res==n:
        print(point)
        break
    point += 1

for i in range(1, point+1):
    if i==(res-n):continue
    print(arr[i], end=' ')