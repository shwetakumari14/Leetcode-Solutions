class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isMirror(root1, root2):
    if root1 is None and root2 is None:
        return True
    
    if root1 is not None and root2 is not None:
        if root1.val == root2.val:
            return isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)
    
    return False

class Solution:
    def isSymmetric(self, root):
        return isMirror(root, root)
        

obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
ans = obj.isSymmetric(root)
print(ans)