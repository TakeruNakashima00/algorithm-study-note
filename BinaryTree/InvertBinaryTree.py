from typing import Optional
from collections import deque

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None

    def insert(self, val) -> TreeNode:

        if self.root is None:
            self.root = TreeNode(val)
            return

        def _insert(node: TreeNode, val):
            if node is None:
                return TreeNode(val)

            if val < node.val:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)
            return node
        return _insert(self.root, val)

    def inorder(self):
        def _inorder(node: TreeNode):
            if node is not None:
                _inorder(node.left)
                print(node.val)
                _inorder(node.right)
        _inorder(self.root)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # swap the children
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root



if __name__ == '__main__':
    binarySearchTree = BinarySearchTree()

    root=[4,2,7,1,3,6,9]
    root = binarySearchTree.insert(4)
    root = binarySearchTree.insert(2)
    root = binarySearchTree.insert(7)
    root = binarySearchTree.insert(1)
    root = binarySearchTree.insert(3)
    root = binarySearchTree.insert(6)
    root = binarySearchTree.insert(9)
    binarySearchTree.inorder()

    print("#########")
    binarySearchTree.invertTree(root)
    binarySearchTree.inorder()

