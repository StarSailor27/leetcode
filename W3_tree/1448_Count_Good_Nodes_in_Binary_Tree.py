# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        
        maxVal = root.val
        
        return self.traversal(root, maxVal)
        
    def traversal(self, root: TreeNode, prevMax) -> int:
        
        GoodNode = 1 if (root.val >= prevMax) else 0
        maxVal = root.val if (GoodNode == 1) else prevMax
        print('root={0}, prevMax={1}, maxVal={2}'.format(root.val, prevMax, maxVal))
        
        if root.left is not None:
            l = self.traversal(root.left, maxVal)
        else:
            l = 0
            
        if root.right is not None:
            r = self.traversal(root.right, maxVal)
        else:
            r = 0
        print('l={0}, r={1}, GoodNode={2}'.format(l, r, GoodNode))        
        return l + r + GoodNode