from sys import stdin
input = lambda:stdin.readline().rstrip()


n, m = map(int, input().split())
l = []
for _ in range(n):
    a, b = map(int,input().split())
    if a>b:l.append([b, a])
l = sorted(l)

result = 0
if l:
    start, end = l[0]
    for idx in range(1, len(l)):
        a, b = l[idx]
        if end<a:
            result += end-start
            start, end = a, b
        elif end<b:end = b
    result += end-start
print(result*2+m)



'''
0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
   |------------------------------->|
         |---------------->|
                     |---------------->|
                                       |<-|
                                 |<-------|
                                 |<-|
      |<----|
   |<----|
'''