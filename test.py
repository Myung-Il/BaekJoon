def a(n):
    if n[0][0]!=10:
        n[0][0]+=1
        b(n)
def b(n):
    if n[0][0]!=10:
        n[0][0]+=1
        a(n)

c = [[0]]
a(c)
print(c)