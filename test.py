from sys import stdin
input = lambda:stdin.readline().rstrip()


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
            if node.left:
                _preorder(node.left)
            if node.right:
                _preorder(node.right)
        _preorder(self.root)


BT = BinaryTree()
BT.root = Node(1)

Node(1).left = Node(2)
Node(1).right = Node(3)

Node(2).left = Node(4)
Node(2).right = Node(5)

Node(3).left = Node(6)
Node(3).right = Node(7)

Node(4).right = Node(9)
Node(5).left = Node(8)

BT.preorder()