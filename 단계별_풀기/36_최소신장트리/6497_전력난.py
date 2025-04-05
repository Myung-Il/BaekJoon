from sys import stdin, setrecursionlimit
input=lambda:stdin.readline().rstrip()
setrecursionlimit(10**6)


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


while 1:
    m, n = map(int,input().split())
    if not(m or n):break
    parents = [i for i in range(m)]
    l = []
    e, s = 0, 0
    for _ in range(n):
        l.append(list(map(int,input().split())))
    l.sort(key=lambda x:x[2]) # 절약을 위해서 가까운 켜둬야만하다
    
    for a, b, w in l:         # 그래서 가까운 것부터 켜둔다
        union(a, b, w)        # 길이 완성되면
        e+=w                  # 전체 요금에서 켜진것 만큼 뺀다
    print(e-s)                # 절약한 요금을 알 수 있다