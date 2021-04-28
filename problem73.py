class TreeNode:
    def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
	def __str__(self):
		if self == None:
			return str(None)
		return f"TreeNode: {{val: {self.val}, Left: {str(self.left)}, Right: {str(self.right)}}}"
		
from queue import Queue
def buildTreeByLevel(lst):
  if len(lst) == 0: return None
  root = TreeNode(lst[0])
  q = Queue()
  q.put(root)
  i = 1
  while i < len(lst):
    parent = q.get()
    if lst[i] != None:
      l = TreeNode(lst[i])
      parent.left = l
      q.put(l)
    i+=1
    if i < len(lst) and lst[i] != None:
      r = TreeNode(lst[i])
      parent.right = r
      q.put(r)
    i+=1
  return root

def equalSubtreeWeight(root):
    if not root:
        return 0
    leftSubtreeWeight = equalSubtreeWeight(root.left)
    rightSubtreeWeight = equalSubtreeWeight(root.right)
    if leftSubtreeWeight !=0 and leftSubtreeWeight == rightSubtreeWeight :
        return True
    if leftSubtreeWeight == True or rightSubtreeWeight == True:
        return True
    return leftSubtreeWeight + rightSubtreeWeight +root.val 
  
lst = [-3,-7,-13,-3,10,1,8,4,5,2,11,None,9,-12,14]
print(equalSubtreeWeight(buildTreeByLevel(lst)))

