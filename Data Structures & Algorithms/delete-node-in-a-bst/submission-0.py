# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val>key:
            root.left=self.deleteNode(root.left, key)
        elif root.val<key:
            root.right=self.deleteNode(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                succ = self.getSuccessor(root.right)
                root.val = succ.val
                root.right = self.deleteNode(root.right, succ.val)

        return root

    def getSuccessor(self, node):
        while node is not None and node.left is not None:
            node = node.left

        return node







