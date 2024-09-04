from sys import stdin
input=lambda:stdin.readline().rstrip()


a1, b1, a2, b2 = map(int,input().split())
a3, b3, a4, b4 = map(int,input().split())

remainder = (a1-a2)*a1-(b1-b2)*b1

for x in range(a1, a2+1):
    if (a1-a2)*b3<= (b1-b2)*x + remainder <=(a1-a2)*b4:
        print(1)
        break
else:print(0)