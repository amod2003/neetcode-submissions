# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l=self.maxDepth(root.left)
        r=self.maxDepth(root.right)
        return 1 + max(l,r)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        op1=self.diameterOfBinaryTree(root.right)
        op2=self.diameterOfBinaryTree(root.left)
        op3=self.maxDepth(root.left)+self.maxDepth(root.right)
        return max(op1,op2,op3)

        