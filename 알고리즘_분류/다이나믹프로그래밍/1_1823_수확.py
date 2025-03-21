from sys import stdin, setrecursionlimit
input = lambda:stdin.readline().strip()
setrecursionlimit(10**6)

n = int(input())
farm = [int(input())for _ in range(n)]

def rice(day, start, end):
    if start==end:return day*farm[start]
    
    left = rice(day+1, start+1, end)
    right = rice(day+1, start, end-1)

    if left > right:return left +day*farm[start]
    else:           return right+day*farm[end]

print(rice(1, 0, n-1))