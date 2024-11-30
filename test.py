from sys import stdin
input = lambda:stdin.readline().rstrip()


n, k = map(int,input().split())

result = []
tree = n
pin = k

print('<', end='')
for _ in range(n):
    result.append(pin)
    pin = pin+k
    while tree and pin>tree:pin -= tree
print(*result, sep=', ', end='>')