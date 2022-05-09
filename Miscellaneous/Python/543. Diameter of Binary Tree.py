class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root):
    if root is None:
        return 0
    
    return 1 + max(height(root.left), height(root.right))

class Solution:
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        
        lheight = height(root.left)
        rheight = height(root.right)

        ldiameter = self.diameterOfBinaryTree(root.left)
        rdiameter = self.diameterOfBinaryTree(root.right)
        
        return max(lheight + rheight, max(ldiameter, rdiameter))

obj = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
ans = obj.diameterOfBinaryTree(root)
print(ans)