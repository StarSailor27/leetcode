# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sizeTree(self, root):
        if (root.left is not None):
            l = self.sizeTree(root.left) + 1
        else:
            l = 1
        if (root.right is not None):
            r = self.sizeTree(root.right) + 1
        else:
            r = 1
        return l if (l >= r) else r