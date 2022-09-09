class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        
        if root1 is not None and root2 is not None:
            if root1.val == root2.val:
                return self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
        
        return False

obj = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
ans = obj.isSameTree(root1, root2)
print(ans)