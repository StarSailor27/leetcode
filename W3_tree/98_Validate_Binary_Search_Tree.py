# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        stParents = []
        return True if (self.traversal(root, stParents) == 0) else False
        
    def traversal(self, root, stParents):
        
        falseNum = 0
        print('root = {0}, stParents = {1}'.format(root.val, stParents))
        # False checker
        if(stParents is not None):
            for rootP in stParents:
                if (rootP[0] == 0): # left
                    if (root.val >= rootP[1]):
                        return 1
                else: #right
                    if (root.val <= rootP[1]):
                        return 1
      
        # in-order traversal
        if (root.left is not None):
            stParents.append((0, root.val))
            falseNum += self.traversal(root.left, stParents)
        
        if (root.right is not None):
            stParents.append((1, root.val))
            falseNum += self.traversal(root.right, stParents)
        
        if (stParents):
            stParents.pop()
        
        return falseNum