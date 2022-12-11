class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        if not root:
            return 0
        
        maxPath = float("-inf")

        def maxSubTreePathSum(node):
            nonlocal maxPath
            if not node:
                return 0
            
            leftSum = max(maxSubTreePathSum(node.left), 0)
            rightSum = max(maxSubTreePathSum(node.right), 0)

            maxPath = max(maxPath, leftSum + rightSum + node.val)

            return max(leftSum + node.val, rightSum + node.val)
        
        maxSubTreePathSum(root)
        return maxPath
    

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
obj = Solution()
ans = obj.maxPathSum(root)
print(ans)