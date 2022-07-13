class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def heightOfTree(self, root):
        if root is None:
            return 0
        else:
            lh = self.heightOfTree(root.left)
            rh = self.heightOfTree(root.right)
            
            return max(lh, rh) + 1

obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
ans = obj.heightOfTree(root)
print(ans)