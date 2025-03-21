from sys import stdin, setrecursionlimit
input = lambda:stdin.readline().strip()
setrecursionlimit(10**6)

n = int(input())
farm = [int(input())for _ in range(n)]
memory = {
    day:{
        start:{
            end:None
            for end in range(n)}
            for start in range(n)}
            for day in range(1, n+1)}

def rice(day, start, end):
    if start==end:return day*farm[start]
    if memory[day][start][end]:return memory[day][start][end]
    
    left = rice(day+1, start+1, end)
    right = rice(day+1, start, end-1)

    if left > right:
        op = left+day*farm[start]
        memory[day][start][end] = op
        return op
    else:
        op = right+day*farm[end]
        memory[day][start][end] = op
        return op

print(rice(1, 0, n-1))

'''
1 3 1 5 2


[ 1  ]
'''