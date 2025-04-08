n = int(input())

if n==2:
    print('''1
1
1
2''')
    exit()

l2 = [num for num in range(1, n+1)if not num%3]
l1 = [num for num in range(1, n+1)if num%3 and num<l2[-1]]

print(len(l1))
print(*l1)
print(len(l2))
print(*l2)