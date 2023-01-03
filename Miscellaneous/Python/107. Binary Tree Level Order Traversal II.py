from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return None
        
        next_level = deque([root])
        levels = []

        while root and next_level:
            curr_level = next_level
            next_level = deque()
            levels.append([])

            for node in curr_level:
                levels[-1].append(node.val)

                if node.left:
                    next_level.append(node.left)
                
                if node.right:
                    next_level.append(node.right)
        
        return levels[::-1]

obj = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
ans = obj.levelOrderBottom(root)
print(ans)