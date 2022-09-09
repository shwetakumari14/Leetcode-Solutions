class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findMaxUntil(root):
    if root is None:
        return 0

    l = findMaxUntil(root.left)
    r = findMaxUntil(root.right)

    maxSingle = max(max(l, r) + root.val, root.val)
    maxTop = max(maxSingle, l + r + root.val)

    findMaxUntil.res = max(findMaxUntil.res, maxTop)

    return maxSingle

class Solution:
    def maxPathSum(self, root):
        
        findMaxUntil.res = float("-inf")

        findMaxUntil(root)

        return findMaxUntil.res

obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
ans = obj.maxPathSum(root)
print(ans)
