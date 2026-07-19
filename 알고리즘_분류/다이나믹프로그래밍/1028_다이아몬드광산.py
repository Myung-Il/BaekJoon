from sys import stdin
input = lambda:stdin.readline().strip()

a, b = map(int, input().split())
l = [list(map(int, input())) for _ in range(a)]
print()


for q in l:
    s=0
    for w in q:
        s+=w
        print(s, end='')
    print()