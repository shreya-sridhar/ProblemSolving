# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    def max_depth_helper(root, depth = 0):
        if root == None:
            return depth
        if root.right:
            return max_depth_helper(root.right, depth + 1)
        if root.left:
            return max_depth_helper(root.left, depth + 1)
        return max(max_depth_helper(root.right, depth + 1),max_depth_helper(root.left, depth + 1))
    return max_depth_helper(root)

root = TreeNode(1,None,TreeNode(2,None,None))
print(maxDepth(root))
