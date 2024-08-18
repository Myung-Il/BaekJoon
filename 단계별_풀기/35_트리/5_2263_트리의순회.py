from sys import stdin, setrecursionlimit
input = lambda:stdin.readline().rstrip()
setrecursionlimit(10**6)


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def preorder(self):
        def _preorder(node):
            print(node.val, end=' ')
            if node.left: _preorder(node.left)
            if node.right:_preorder(node.right)
        _preorder(self.root)

def make(left, right):
    global top
    if left>=right:return

    top-=1
    find = postorder[top]    # 뿌리에 가까우면서 가장 오른쪽에 있는 것
    node = Node(find)        # 그것을 노드로 만듬

    idx = inorder_post[find]        # 그것을 기준으로 왼쪽인지 오른쪽인지 구분
    node.right = make(idx+1, right) # 오른쪽의 정보를 우선 처리 해준다
    node.left = make(left, idx)     # top이 postorder의 정보를 하나씩 처리하기 때문에
    return node                     # 순서를 맞추려면 오른쪽부터 찾아야 한다


n = int(input())                           # 규칙이 있음
inorder = list(map(int,input().split()))   # 깊이 구분없이 노드의 왼쪽인가 오른쪽인가만으로 배치 되어 있음
postorder = list(map(int,input().split())) # 뿌리에 가까우면서 오른쪽 우선으로 배치되어 있음
inorder_post = {inorder[idx]:idx for idx in range(n)} # 오른쪽부터 채우면서 트리를 만들 수 있음

top = n
BT = BinaryTree()
BT.root = make(0, n)
BT.preorder()