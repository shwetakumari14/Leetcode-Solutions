class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Height:
    def __init__(self):
        self.height = 0
        
def height(root):
    if root is None:
        return 0
        
    return max(height(root.left), height(root.right)) + 1

class Solution:
    def isBalanced(self,root):
    
        if root is None:
            return 1
        
        lh, rh = Height(), Height()
        
        lh.height = height(root.left)
        rh.height = height(root.right)
        
        l = self.isBalanced(root.left)
        r = self.isBalanced(root.right)
        
        if abs(lh.height - rh.height) <= 1:
            return l and r
        
        return 0

obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
ans = obj.isBalanced(root)
print(ans)