from sys import stdin
input=lambda:stdin.readline().rstrip()

def solve():
    for idx1 in range(n):     # 비교를 할
        for idx2 in range(n): # 두 선분
            if parents[idx1]==parents[idx2]:continue # 두 선분 사이에 교점이 있다면 지나친다
            a1, b1, a2, b2 = point[idx1][0][0], point[idx1][0][1], point[idx1][1][0], point[idx1][1][1]
            a3, b3, a4, b4 = point[idx2][0][0], point[idx2][0][1], point[idx2][1][0], point[idx2][1][1]
            
            a = ccw(a1, b1, a2, b2, a3, b3)
            b = ccw(a1, b1, a2, b2, a4, b4)
            c = ccw(a3, b3, a4, b4, a1, b1)
            d = ccw(a3, b3, a4, b4, a2, b2)

            mx1, my1, mx2, my2 = min(a1, a2), min(b1, b2), max(a1, a2), max(b1, b2)
            mx3, my3, mx4, my4 = min(a3, a4), min(b3, b4), max(a3, a4), max(b3, b4)

            if a*b == 0 and c*d == 0:
                if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:union(idx1, idx2) # 교점이 존재한다면 두 선분이
            elif a*b <= 0 and c*d <= 0:                                    union(idx1, idx2) # 같은 집합에 있도록 설정해준다
    return parents

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3

def find(e):
    if e!=parents[e]:
        parents[e] = find(parents[e])
    return parents[e]

def union(x, y):
    x = find(x)
    y = find(y)
    if x<y:parents[y] = x
    else:  parents[x] = y


n = int(input())
point = [0]*n
parents = [i for i in range(n)]
for idx in range(n):
    a1, b1, a2, b2 = map(int, input().split())
    point[idx] = [[a1, b1], [a2, b2]]

result = solve()                    # 집합을 설정했는데 마지막에 집합 3개를 합칠 수 도 있다
result = [find(i)for i in range(n)] # 그러니 집합이 서로 같은 것인지 확인해준다
d = {}
for elm in result:
    if not d.get(elm):d[elm] = 0
    d[elm] += 1
print(len(d))
print(max(d.values()))