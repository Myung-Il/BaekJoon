from sys import stdin
input=lambda:stdin.readline().rstrip()

a1, b1 = map(int,input().split())
a2, b2 = map(int,input().split())
a3, b3 = map(int,input().split())

result = (a1*b2+a2*b3+a3*b1) - (b1*a2+b2*a3+b3*a1)
if result>0: print(1)
if result==0:print(0)
if result<0:print(-1)