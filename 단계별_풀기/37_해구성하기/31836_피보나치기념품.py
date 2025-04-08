n = int(input())

l = [i for i in range(n+1)]

l1, l2 = [], []
for idx in range(n, 2, -3):
    l1.append(l.pop())
    l2.append(l.pop())
    l2.append(l.pop())
if len(l)==3:
    l1.append(l.pop())
    l2.append(l.pop())
    
print(len(l1))
print(*l1)
print(len(l2))
print(*l2)