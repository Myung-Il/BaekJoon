from sys import stdin
input = lambda:stdin.readline().rstrip()


def testCase(m):
    l = []
    m = m//10+(1 if m%10 else 0)
    for _ in range(m):
        for elm in tuple(map(int,input().split())):
            l.append(elm)
    return l


for _ in range(int(input())):
    m = int(input())
    testcase = testCase(m)
    queue = []
    result = []

    for idx in range(m):
        queue.append(testcase[idx])
        queue = sorted(queue)
        if not idx%2:result.append(queue[idx//2])
    
    print(m//2+1)
    print(*result)