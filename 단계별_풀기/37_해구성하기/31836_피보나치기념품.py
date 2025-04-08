n = int(input())

l = [num for num in range(n+1)]

l1, l2 = [], []
for idx in range(3, n+1, 3):
    l1.append(l[idx])
    l2.append(l[idx-1])
    l2.append(l[idx-2])

print(l)
print(l1)
print(l2)