# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        n = len(preorder)
        if n == 0: return None

        hashmap = {}
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i

        def helper(preorder, inorder, ii, ij):
            if ii > ij: return None

            val = preorder.popleft()
            root = TreeNode(val)

            index = hashmap[val]

            root.left = helper(preorder, inorder, ii, index-1)
            root.right = helper(preorder, inorder, index+1, ij)

            return root

        root = helper(collections.deque(preorder), inorder, 0, n-1)
        return root

        
        
        