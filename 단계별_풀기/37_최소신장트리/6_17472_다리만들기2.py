from sys import stdin, setrecursionlimit
from collections import deque
input=lambda:stdin.readline().rstrip()
setrecursionlimit(10**6)


def dfs(x, y):
    if 0>x or x>=m or 0>y or y>=n: return False
    if land[y][x]:
        land[y][x] = 0
        make[y][x] = land_num
        island[land_num].append([x, y])
        for i in range(4):
            xi = x+xl[i]
            yi = y+yl[i]
            dfs(xi, yi)
            
        return True
    return False

def bfs(il):
    for x, y in island[il]:
        for i in range(4):
            xi = x+xl[i]
            yi = y+yl[i]
            distance = 0
            while True:
                if 0>xi or xi>=m or 0>yi or yi>=n: break
                now = make[yi][xi]

                if now==il:break
                if now==0:
                    xi+=xl[i]
                    yi+=yl[i]
                    distance+=1
                elif distance<2:break
                else:
                    bridge.append([il, now, distance])
                    break

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
    s+=w


xl = [ 1,-1, 0, 0]
yl = [ 0, 0,-1, 1]

n, m = map(int,input().split())
land = []
make  = [[0]*m for _ in range(n)]
visit = [[0]*m for _ in range(n)]
for _ in range(n):
    land.append(list(map(int,input().split())))

island = [[]for _ in range(51)]
land_num = 1
for yi in range(n):
    for xi in range(m):
        if dfs(xi, yi):
            land_num+=1

bridge = []
for il in range(1, land_num-1):
    bfs(il)
bridge.sort(key=lambda x:x[2])

parents = [idx for idx in range(land_num)]
s = 0
for a, b, w in bridge:
    union(a, b, w)

print(s if s else -1)