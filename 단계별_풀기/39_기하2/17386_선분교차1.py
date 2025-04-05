from sys import stdin
input=lambda:stdin.readline().rstrip()


def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3


a1, b1, a2, b2 = map(int,input().split())
a3, b3, a4, b4 = map(int,input().split())

a = ccw(a1, b1, a2, b2, a3, b3) # 1번 선분보다 왼쪽이나 오른쪽에 있으면 양수와 음수로 표현된다
b = ccw(a1, b1, a2, b2, a4, b4) # 둘 다 양수라면 2번 선분이 왼쪽에 있는 거고 둘 다 음수라면
c = ccw(a3, b3, a4, b4, a1, b1) # 2번 선분이 오른쪽에 있다는 거다
d = ccw(a3, b3, a4, b4, a2, b2) # 양수끼리 음수끼리 곱하면 양수가 나온다
print(1 if a*b<0 and c*d<0 else 0) # 각 두개를 곱해서 양수가 나오면 교차점이 없다는 것이다