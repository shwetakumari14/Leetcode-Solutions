class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k):
       self.k = k
       self.res = None
       self.findSmallest(root)

       return self.res 

    def findSmallest(self, root):
        if not root:
            return None
        
        self.findSmallest(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.findSmallest(root.right)
       

obj = Solution()
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
ans = obj.kthSmallest(root, 2)
print(ans)
