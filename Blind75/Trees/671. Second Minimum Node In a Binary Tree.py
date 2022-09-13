class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root):
        self.ans, min1 = float("inf"), root.val

        def dfs(node):
            if node:
                if min1 < node.val < self.ans:
                    self.ans = node.val
                elif node.val == min1:
                    dfs(node.left)
                    dfs(node.right)
        
        dfs(root)

        if self.ans < float("inf"):
            return self.ans
        
        return -1

       

obj = Solution()
root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
ans = obj.findSecondMinimumValue(root)
print(ans)
