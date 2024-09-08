from sys import stdin
input=lambda:stdin.readline().rstrip()

def solve():
    parents = [-1]*n
    parents[0] = 0
    for idx1 in range(n-1):
        for idx2 in range(idx1+1, n):
            if parents[idx1]==parents[idx2]:continue
            a1, b1, a2, b2 = point[idx1][0][0], point[idx1][0][1], point[idx1][1][0], point[idx1][1][1]
            a3, b3, a4, b4 = point[idx2][0][0], point[idx2][0][1], point[idx2][1][0], point[idx2][1][1]
            
            a = ccw(a1, b1, a2, b2, a3, b3)
            b = ccw(a1, b1, a2, b2, a4, b4)
            c = ccw(a3, b3, a4, b4, a1, b1)
            d = ccw(a3, b3, a4, b4, a2, b2)

            mx1, my1, mx2, my2 = min(a1, a2), min(b1, b2), max(a1, a2), max(b1, b2)
            mx3, my3, mx4, my4 = min(a3, a4), min(b3, b4), max(a3, a4), max(b3, b4)

            if a*b == 0 and c*d == 0:
                if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
                    if parents[idx1]==-1:parents[idx1] = parents[idx2]
                    else:                parents[idx2] = parents[idx1]
            elif a*b <= 0 and c*d <= 0:
                    if parents[idx1]==-1:parents[idx1] = parents[idx2]
                    else:                parents[idx2] = parents[idx1]
    return parents

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3


n = int(input())
point = [0]*n
for idx in range(n):
    a1, b1, a2, b2 = map(int, input().split())
    point[idx] = [[a1, b1], [a2, b2]]

result = solve()
l = [0]*(n+1)
for elm in result:
    l[elm] += 1

s, mx = 0, max(l[:n])
for idx in range(n):
    if l[idx]:s+=1
print(s+l[-1])
print(mx if mx else 1)
print(result)