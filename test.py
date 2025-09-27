s = 0
for i in range(1415):
    s += i+1
print(s)


n = 0
while s>=1000000:
    s -= n
    n += 1

print(s)