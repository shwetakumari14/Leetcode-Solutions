class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestorInBinaryTree(self, root, p, q):
        if root is None:
            return None
        
        if root.val == p or root.val == q:
            return root
        
        left = self.lowestCommonAncestorInBinaryTree(root.left, p, q)
        right = self.lowestCommonAncestorInBinaryTree(root.right, p, q)

        if left and right:
            return root
        
        return left or right

       

obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
ans = obj.lowestCommonAncestorInBinaryTree(root, 2, 3)
print(ans)
