class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
       self.ans = 0
    
    def height(self, root):
       if root is None: 
           return 0
           
       lh = self.height(root.left)
       rh = self.height(root.right)
       
       self.ans = max(self.ans, 1 + lh + rh)
       return 1 + max(lh, rh)
       
    def diameter(self,root):
        self.height(root)
        
        return self.ans

obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
ans = obj.diameter(root)
print(ans)