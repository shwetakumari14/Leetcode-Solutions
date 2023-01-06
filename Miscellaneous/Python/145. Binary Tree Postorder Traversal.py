class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root):
        if not root:
            return None
        
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        print(root.val, end=" ")
        

obj = Solution()
root = TreeNode(1)
root.right = TreeNode(5)
root.right.left = TreeNode(4)
ans = obj.postorderTraversal(root)
print()