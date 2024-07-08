from sys import stdin
input = lambda:stdin.readline().rstrip()

n = int(input())
l = [list(map(int,input().split()))for _ in range(n)]

k = [[0]*n for _ in range(n)]

for idx in range(n-1):
    k[idx][idx+1] = l[idx][0]*l[idx][1]*l[idx+1][1]

for x in range(2, n):
    for y in range(n-x):
        k[y][x+y] = min([k[y][idx]+k[idx+1][x+y] + l[y][0]*l[idx][1]*l[x+y][1] for idx in range(y, x+y)])

for i in k:print(i)

'''
7
9 3
3 7
7 8
8 2
2 4
4 6
6 7
'''