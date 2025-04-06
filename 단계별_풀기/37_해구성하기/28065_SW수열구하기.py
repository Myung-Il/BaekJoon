n = int(input())
l = [0]*n

f, b = 0, n+1
for idx in range(1, n, 2):l[idx] += (f:=f+1)
for idx in range(0, n, 2):l[idx] += (b:=b-1)

print(*l)