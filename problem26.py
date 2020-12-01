# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: TreeNode) -> bool:
    def isbst_helper(root, lower_bound, upper_bound):
        if root is None:
            return True
        else:
            return root.val < upper_bound and root.val > lower_bound and isbst_helper(root.right, root.val, upper_bound) and isbst_helper(root.left, lower_bound, root.val)    
        
    lower_bound = float('-inf')
    upper_bound = float('+inf')
    return isbst_helper(root,lower_bound, upper_bound)
        
root = TreeNode(2,TreeNode(1,None,None),TreeNode(3,None,None))
print(isValidBST(root))       

