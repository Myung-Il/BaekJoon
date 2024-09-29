from sys import stdin
input=lambda:stdin.readline().rstrip()


def gcd(a, b):
    if a==0:return b
    return gcd(b%a, a)

def bit(x, visit):
    if visit==(1<<n)-1:
        global s, c
        if not int(x)%k:c+=1
        s+=1
        return
    
    for idx in range(n):
        if visit&1<<idx:continue
        bit(x+l[idx], visit|1<<idx)


n = int(input())
l = [input()for _ in range(n)]
k = int(input())

s, c = 0, 0
bit("", 0)

t = gcd(c, s)
if c:print(f"{c//t}/{s//t}")
else:print("0/1")