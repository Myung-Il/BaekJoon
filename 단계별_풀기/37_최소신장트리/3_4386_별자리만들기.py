from sys import stdin, setrecursionlimit
input=lambda:stdin.readline().rstrip()
setrecursionlimit(10**6)


def distance(x1, y1, x2, y2):
    return ( (x1-x2)**2 + (y1-y2)**2 )**0.5

def find(e):
    if e!=parents[e]:
        parents[e] = find(parents[e])
    return parents[e]

def union(x, y, w):
    x = find(x)
    y = find(y)
    if x==y:return

    if x<y:parents[y] = x
    else:  parents[x] = y
    
    global s
    s += w


n = int(input())
l = [list(map(float,input().split()))for _ in range(n)]
star = []
for idx1 in range(n-1):           # 각 별끼리의 거리를 구함
    for idx2 in range(idx1+1, n): # 시점별, 도착별, 거리 순으로 저장
        star.append( [idx1+1, idx2+1, distance(*l[idx1], *l[idx2])] ) 

star.sort(key=lambda x:x[2])          # 거리순으로 정리
parents = [idx for idx in range(n+1)] # 크루스칼 알고리즘 사용
s = 0
for a, b, w in star:
    union(a, b, w)
print("%.2f"%s)