class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        
        children = [root.left, root.right]

        if not any(children):
            return 1
        
        minDepth = float("inf")
        for child in children:
            if child:
                minDepth = min(minDepth, self.minDepth(child))

        return minDepth + 1
        

obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
ans = obj.minDepth(root)
print(ans)