class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self,root):        
        queue, ans = [], []
        
        queue.append(root)
        
        while queue:
            node = queue.pop(0)
            ans.append(node.val)
            
            if node.left is not None:
                queue.append(node.left)
            
            if node.right is not None:
                queue.append(node.right)
        
        return ans

obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
ans = obj.levelOrder(root)
print(ans)