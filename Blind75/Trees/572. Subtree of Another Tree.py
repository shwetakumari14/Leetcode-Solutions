class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    
    if root1 is not None and root2 is not None:
        if root1.val == root2.val:
            return isSymmetric(root1.left, root2.left) and isSymmetric(root1.right, root2.right)
    

class Solution:
    def isSubtree(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        
        if root is None and subRoot is not None:
            return False
        
        if isSymmetric(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)    
       

obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
subRoot = TreeNode(1)
ans = obj.isSubtree(root, subRoot)
print(ans)