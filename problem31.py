# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
def flatten(root):
    def flatten_helper(root):
        if not root.left and not root.right:
            return
        elif root.left:
            left_tree = root.left
            left_tree_head = left_tree
            while left_tree.right:
                left_tree = left_tree.right
            left_tree.right = root.right
            root.right = left_tree_head
            root.left = None
        root = root.right 
        flatten_helper(root)
    flatten_helper(root)
        
root = TreeNode(1,TreeNode(2,TreeNode(3,None,None),TreeNode(4,None,None)),TreeNode(5,None,TreeNode(6,None,None)))
flatten(root)
i = 0
print(root.val)
while i<5:
    print(root.right.val)
    root = root.right
    i+=1

