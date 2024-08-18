from sys import stdin, setrecursionlimit
input = lambda:stdin.readline().rstrip()
setrecursionlimit(10**6)


def make(left, right):
    global top
    if left>=right:return

    top-=1
    find = postorder[top]
    print(find)

    idx = inorder_post[find]
    make(idx+1, right)
    make(left, idx)
    


n = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))
inorder_post = {inorder[idx]:idx for idx in range(n)}

top = n
make(0, n)