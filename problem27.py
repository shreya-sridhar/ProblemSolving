# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_sym_helper(r1, r2):
            if not r1 and not r2:
                return True
            elif r1 and r2:
                return r1.val == r2.val and is_sym_helper(r1.right, r2.left) and is_sym_helper(r2.right, r1.left)
            else:
                return False
        if not root:
            return True
        return is_sym_helper(root.left, root.right)
        
        
        
        