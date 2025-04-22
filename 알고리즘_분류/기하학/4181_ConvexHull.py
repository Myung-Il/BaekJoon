from sys import stdin
input = lambda:stdin.readline().rstrip()

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3


def monotoneChain():
    stack = []

    for px, py in points:
        while len(stack)>1 and ccw(*stack[-2], *stack[-1], px, py) < 0:
            stack.pop()
        stack.append((px, py))
    
    return stack


n = int(input())
points = []
for _ in range(n):
    x, y, c = input().split()
    if c=="Y":points.append(list(map(int, (x, y))))
points.sort()


stack = monotoneChain()
for x, y in points[::-1]:
    if (x, y) not in stack:
        stack.append((x, y))

print(len(stack))
for point in stack:
    print(*point)