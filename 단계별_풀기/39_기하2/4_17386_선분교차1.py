from sys import stdin
input=lambda:stdin.readline().rstrip()


a1, b1, a2, b2 = map(int,input().split())
a3, b3, a4, b4 = map(int,input().split())

remainder1 = (a1-a2)*a1-(b1-b2)*b1
remainder2 = (a3-a4)*a3-(b3-b4)*b3

for x in range(a1, a2+1):
    if (b1-b2)*(a3-a4)*x - (b3-b4)*(a1-a2)*x - (remainder2*(a1-a2) - remainder1*(a3-a4)) == 0:
        print(1)
        break
else:print(0)