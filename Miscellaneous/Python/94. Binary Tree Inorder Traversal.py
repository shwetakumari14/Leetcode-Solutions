class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.val)
            self.inorderTraversal(root.right)

obj = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
obj.inorderTraversal(root)
