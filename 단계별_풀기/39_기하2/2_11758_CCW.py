from sys import stdin
input=lambda:stdin.readline().rstrip()

a1, b1 = map(int,input().split())
a2, b2 = map(int,input().split())
a3, b3 = map(int,input().split())

slope = (b2-b1)/(a2-a1)
b = b1 - slope*a1
lost = slope*a3 + b

if slope>0:
    if lost<b3:print(1)
    if lost==b3:print(0)
    if lost>b3:print(-1)

if slope<0:
    if lost>b3:print(1)
    if lost==b3:print(0)
    if lost<b3:print(-1)