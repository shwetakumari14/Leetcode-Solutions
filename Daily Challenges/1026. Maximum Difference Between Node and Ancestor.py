class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root):
        if not root:
            return 0
        
        def helperFunc(node, currMax, currMin):
            if not node:
                return currMax - currMin
            
            currMax = max(currMax, node.val)
            currMin = min(currMin, node.val)

            left = helperFunc(node.left, currMax, currMin)
            right = helperFunc(node.right, currMax, currMin)

            return max(left, right)
        
        return helperFunc(root, root.val, root.val)


root = TreeNode(8)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right = TreeNode(10)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

obj = Solution()
ans = obj.maxAncestorDiff(root)
print(ans)