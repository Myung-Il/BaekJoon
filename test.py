ipt = "a b 5".split()
a, b, c = (lambda s1, s2, i: (s1, s2, int(i)))(*ipt)

print(f"a(={a}) : {type(a)}")
print(f"b(={b}) : {type(b)}")
print(f"c(={c}) : {type(c)}")