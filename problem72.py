class TreeNode:
    def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
	def __str__(self):
		if self == None:
			return str(None)
		return f"TreeNode: {{val: {self.val}, Left: {str(self.left)}, Right: {str(self.right)}}}"
		





