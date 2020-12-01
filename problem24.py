# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder_helper(root, traversal):
            if not root:
                return
            inorder_helper(root.left, traversal)
            traversal.append(root.val)
            inorder_helper(root.right, traversal)
            return traversal
        traversal = []
        return inorder_helper(root,traversal)
        
        
        
        


