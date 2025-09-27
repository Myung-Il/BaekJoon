from sys import stdin
input = lambda:stdin.readline().strip()

n = int(input())
for i in range(1, n+1):
    if i+i*i >= n:break

print(i*2)
for _ in range(i):print(1, end=' ')
for _ in range(i):print(i, end=' ')


'''
2 : 1 1
4 : 1 1 2 2
7 : 1 1 1 3 3 3
13 : 1 1 1 1 4 4 4 4
21 : 1 1 1 1 1 5 5 5 5 5
'''