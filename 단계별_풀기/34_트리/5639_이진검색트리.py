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

    def postorder(self):
        def _postorder(node):
            if node.left:  _postorder(node.left)
            if node.right: _postorder(node.right)
            print(node.val, end=' ')
        _postorder(self.root)

def make(left, right):
    if left>=right:return

    node = Node(tree[left])

    elm = right                      # 맨앞의 어떤 수보다 크다면 그 수의 오른쪽 트리임
    for idx in range(left+1, right): # 그렇다면 당연히 맨앞의 어떤 수 다음부터
        if tree[left]<tree[idx]:     # 큰 수가 나오기 전까지가 왼쪽 트리임
            elm = idx                # 큰 수가 나오는 위치 기록
            break

    node.left = make(left+1, elm) # 왼쪽 트리
    node.right = make(elm, right) # 오른쪽 트리
    return node  


tree = []
while 1:
    try:tree.append(int(input()))
    except:break

BT = BinaryTree()
BT.root = make(0, len(tree))
BT.postorder()