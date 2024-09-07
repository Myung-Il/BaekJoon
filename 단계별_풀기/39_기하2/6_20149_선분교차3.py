from sys import stdin
input=lambda:stdin.readline().rstrip()

def solve():
    if a*b == 0 and c*d == 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return 1
    else:
        if a*b <= 0 and c*d <= 0:
            return 1

    return 0

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3

def cross():
    px = (a1*b2-b1*a2)*(a3-a4) - (a1-a2)*(a3*b4-b3*a4)
    py = (a1*b2-b1*a2)*(b3-b4) - (b1-b2)*(a3*b4-b3*a4)
    p =  (a1-a2)*(b3-b4) - (b1-b2)*(a3-a4)
    if p:return px/p, py/p
    
    point = []
    for idx in range(3):
        if l[idx] in l[idx+1:]:point.append(l[idx])
    if len(point)==1:return point[0]
    return 0, 0


a1, b1, a2, b2 = map(int,input().split())
a3, b3, a4, b4 = map(int,input().split())


mx1, my1, mx2, my2 = min(a1, a2), min(b1, b2), max(a1, a2), max(b1, b2)
mx3, my3, mx4, my4 = min(a3, a4), min(b3, b4), max(a3, a4), max(b3, b4)

a = ccw(a1, b1, a2, b2, a3, b3)
b = ccw(a1, b1, a2, b2, a4, b4)
c = ccw(a3, b3, a4, b4, a1, b1)
d = ccw(a3, b3, a4, b4, a2, b2)

l = [(a1, b1), (a2, b2), (a3, b3), (a4, b4)]
result = solve()
print(result)
if result:
    x, y = cross()
    if x or y:print(x, y)
    elif (0, 0)in l:print(0, 0)