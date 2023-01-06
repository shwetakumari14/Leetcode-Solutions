class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        if not root:
            return None
        
        print(root.val, end=" ")
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        

obj = Solution()
root = TreeNode(1)
root.right = TreeNode(5)
root.right.left = TreeNode(4)
ans = obj.preorderTraversal(root)
print()