from sys import stdin, setrecursionlimit
input = lambda:stdin.readline().rstrip()
setrecursionlimit(10**6)


def union(x, y):
    x, y = find(x), find(y) # 가장 위의 조상 노드를 찾으러 감
    if x<y:parents[y] = x   # 더 작은 숫자가 조상이 되도록 설정
    else:  parents[x] = y

def find(x):
    if parents[x]!=x:                 # 본인이 조상노드가 아니라면
        parents[x] = find(parents[x]) # 찾으러감
    return parents[x]                 # 조상 노드를 반환


n, m = map(int,input().split())
parents = [num for num in range(n+1)]
for _ in range(m):
    rl, a, b = map(int,input().split())
    if rl:print("YES"if find(a)==find(b)else"NO")
    else: union(a, b)