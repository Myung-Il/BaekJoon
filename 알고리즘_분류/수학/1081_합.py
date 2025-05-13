# l, u = map(int, input().split())
l, u = 0, 110
res = 0
for num in range(l, u+1):
    for n in str(num):
        res += int(n)

print(res)
# print(900+45+45*11)

'''
111
112
113
114
115
116
117
118
119
120
'''