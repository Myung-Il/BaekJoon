from sys import stdin, setrecursionlimit
input = lambda:stdin.readline().rstrip()
setrecursionlimit(10**6)

def dfs(e, w):
    left, right = 0, 0
    for node, weight in l[e]:
        radius = 0
        if not visit[node]:
            visit[node] = 1
            radius = dfs(node, weight)
        if left<=right:left = max(left, radius)
        else:right = max(right, radius)
    
    global mx
    mx = max(mx, left+right)
    return max(left+w, right+w)


n = int(input())
l = [[]for _ in range(n+1)]
visit = [0]*(n+1)
for _ in range(n-1):                   # 바로 이전 문제인 1167번과 입력 방식만
    a, b, w = map(int,input().split()) # 다를 뿐 같은 문제다
    l[a].append([b, w])

mx = 0
visit[1] = 1
dfs(1, 0)
print(mx)