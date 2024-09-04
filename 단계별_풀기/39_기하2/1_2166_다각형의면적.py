from sys import stdin
input=lambda:stdin.readline().rstrip()


n = int(input())
l = [list(map(int, input().split()))for _ in range(n)]
l.append(l[0])

a, b = 0, 0
for idx in range(n):
    a += l[idx][0]*l[idx+1][1]
    b += l[idx+1][0]*l[idx][1]

print("%0.1f"%abs((a-b)/2))