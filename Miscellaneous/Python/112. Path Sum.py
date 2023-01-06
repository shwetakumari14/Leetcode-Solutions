class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        targetSum -= root.val

        if root.left is None and root.right is None:
            return targetSum == 0
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        

obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
targetSum = 3
ans = obj.hasPathSum(root, targetSum)
print(ans)