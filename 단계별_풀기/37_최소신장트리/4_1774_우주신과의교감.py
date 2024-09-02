from sys import stdin, setrecursionlimit
input=lambda:stdin.readline().rstrip()
setrecursionlimit(10**6)


def distance(x1, y1, x2, y2):
    return ( (x1-x2)**2 + (y1-y2)**2 )**0.5

def find(e):
    if e!=parents[e]:
        parents[e] = find(parents[e])
    return parents[e]

def union(x, y, w=0):
    x = find(x)
    y = find(y)
    if x==y:return

    if x<y:parents[y] = x
    else:  parents[x] = y
    
    global s
    s += w


n, m = map(int,input().split())
l = [list(map(int,input().split()))for _ in range(n)]
star = []
parents = [idx for idx in range(n+1)]
s = 0
for idx1 in range(n-1):
    for idx2 in range(idx1+1, n):
        star.append( [idx1+1, idx2+1, distance(*l[idx1], *l[idx2])] ) 
for _ in range(m):                  # 이전 문제 4386번에서
    a, b = map(int,input().split()) # 이미 연결되어 있는 부분을 추가하면 되는 일이다
    union(a, b)

star.sort(key=lambda x:x[2])
for a, b, w in star:
    union(a, b, w)
print("%.2f"%s)