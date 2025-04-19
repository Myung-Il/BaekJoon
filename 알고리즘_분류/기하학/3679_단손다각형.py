from sys import stdin
input=lambda:stdin.readline().rstrip()

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 -x2*y1-x3*y2-x1*y3


def monotoneChain():
    stack = []
    result = []

    for px, py, idx in points:
        while len(stack)>1 and ccw(*stack[-2], *stack[-1], px, py) < 0:
            stack.pop()
            result.pop()
        stack.append((px, py))
        result.append(idx)
    
    return result


for _ in range(int(input())):
    n, *txt = list(map(int, input().split()))
    points = sorted(zip(txt[::2], txt[1::2], range(n)))

    # 아래 껍질을 먼저 만든다
    num = monotoneChain()

    # 나머지는 그냥 순서 대로 넣으면 된다
    for _, _, idx in points[::-1]:
        if idx not in num:num.append(idx)
    
    print(*num)