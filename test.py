from sys import stdin
input = lambda:stdin.readline().rstrip()

def Distance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def DFS(deep, sum, a, b, l):
    global ans, assign
    if deep==w:
        if ans>sum:
            ans, assign = sum, l
        return
    elif sum>ans:return

    location = incident[deep]
    DFS(deep+1, sum+Distance(location, a), location, b, l+[1])
    DFS(deep+1, sum+Distance(location, b), a, location, l+[2])


n = int(input()) # 도로의 개수
w = int(input()) # 사건의 수
incident = [list(map(int,input().split()))for _ in range(w)] # 사건의 좌표

ans, assign = float("inf"), []
DFS(0, 0, [1, 1], [n, n], [])
print(ans)
print(*assign, sep='\n')